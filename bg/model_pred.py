import joblib
import pandas as pd
import os
import pymysql
import sklearn
import requests
import json
import time
import pytz
from datetime import datetime
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

# 서울의 타임존 설정
seoul_timezone = pytz.timezone('Asia/Seoul')

# 현재 서울의 시간
seoul_time = datetime.now(seoul_timezone)

current_time = seoul_time.strftime('%Y.%m.%d %H.%M.%S')


loaded_model = joblib.load('./random_forest_model.pkl')

# 현재 시간을 '년-월-일 시:분:초' 형식으로 출력

connection = pymysql.connect(
    # use aws DB connection for get Data from mysql server
)
def get_confusion(row, traffic_df):
    # cur_parking_time을 datetime으로 변환 (만약 이미 datetime 형식이라면 이 줄은 생략 가능)
    row['cur_parking_time'] = pd.to_datetime(row['cur_parking_time'])

    # traffic_df에서 createdDate가 datetime 형식인지 확인하고, 변환 필요 시 변환
    traffic_df['createdDate'] = pd.to_datetime(traffic_df['createdDate'])

    # 동일한 park_name을 가진 traffic_df 데이터 필터링
    matched_traffic = traffic_df[
        (traffic_df['park_name'] == row['park_name']) & 
        (row['cur_parking_time'] - pd.Timedelta(minutes=25) <= traffic_df['createdDate']) & 
        (traffic_df['createdDate'] <= row['cur_parking_time'] - pd.Timedelta(minutes=5))
    ]
    
    # confusion 값을 반환, 없으면 NaN 반환
    if not matched_traffic.empty:
        return matched_traffic['confusion'].values[0]
    else:
        return None
try:
    # SQL 쿼리 실행
    query = "SELECT * FROM tb_pred_weather_parking"
    park_weather_df = pd.read_sql(query, connection)
    query = "SELECT * FROM tb_pred_traffic"
    traffic_df = pd.read_sql(query, connection)
    park_weather_df['confusion'] = park_weather_df.apply(get_confusion, axis=1, traffic_df=traffic_df)
    park_weather_df.drop(columns=["10m_w"])
    totoal_df=park_weather_df.tail(32)
    
    df= totoal_df.drop(columns=['cur_parking_new'])
    df.rename(columns={
    '10m_w': '10m/w',
    '15m_r': '15m/r',
    '1h_r': '1h/r',
    }, inplace=True)
    # 'cur_parking_time'을 datetime 형식으로 변환
    df['cur_parking_time'] = pd.to_datetime(df['cur_parking_time'])

    # 여의도에서 가장 큰 축제인 불꽃축제가 열린 날은 주차장 데이터가 이상치가 나왔기 때문에 제외
    df = df[df['cur_parking_time'].dt.date != pd.to_datetime('2024-10-05').date()]


    #시간을 20분 단위로 반올림
    def round_minute(dt):
        minute = dt.minute
        if 0 <= minute < 20:
            return dt.replace(minute=0, second=0)
        elif 20 <= minute < 40:
            return dt.replace(minute=20, second=0)
        else:
            return dt.replace(minute=40, second=0)

    df['cur_parking_time'] = df['cur_parking_time'].apply(round_minute)

    # cur_parking_time 열을 기준으로 시간별로 정렬
    df = df.sort_values(by='cur_parking_time')

    # 새로운 열 추가: weekday, hour, minute
    df['hour'] = df['cur_parking_time'].dt.hour
    df['minute'] = df['cur_parking_time'].dt.minute
    df['purpose'] = df['purpose'].astype('float')
    df = pd.get_dummies(df, columns=['park_name', 'purpose', 'park_type', 'weekday', 'hour', 'minute'], drop_first=True)
    # 라벨 0값 처리
    for i in df.columns:
        if i in ["weekday_0","hour_0","minute_0"]:
            df.drop([i],axis=1,inplace=True)
    
    df.rename(columns={
    'now_r': 'now/r',
    }, inplace=True)
    
    null_target=['weekday_1', 'weekday_2', 'weekday_3', 'weekday_4',
       'weekday_5', 'weekday_6', 'hour_1', 'hour_2', 'hour_3', 'hour_4',
       'hour_5', 'hour_6', 'hour_7', 'hour_8', 'hour_9', 'hour_10', 'hour_11',
       'hour_12', 'hour_13', 'hour_14', 'hour_15', 'hour_16', 'hour_17',
       'hour_18', 'hour_19', 'hour_20', 'hour_21', 'hour_22', 'hour_23',
       'minute_20', 'minute_40',"park_name_영등포 롯데역사 주차장"]
    
    # 수치형 변수들 스케일링을 통한 정규화
    scaler = StandardScaler()
    df.drop(['cur_parking_time', 'time_rate'], axis=1, inplace=True)
    features_to_scale = ['capacity', 'rates', 'add_rates', '10m/w']
    df[features_to_scale] = scaler.fit_transform(df[features_to_scale])
    trained_features=loaded_model.feature_names_in_
    for i in null_target:
        if i not in df.columns:
          df[i] = False
    df=df[trained_features]
    y_pred = loaded_model.predict(df)
    y_pred = np.round(y_pred)
    # 예측 결과를 DataFrame으로 변환
    y_pred_df = pd.DataFrame(y_pred, columns=["pred_parking"])

    # totoal_df와 예측 결과를 옆에 붙이기 (index가 같아야 함)
    totoal_df["pre_parking_time"] = totoal_df["cur_parking_time"] + pd.to_timedelta(20, unit='m')
    result_df = pd.concat([totoal_df.reset_index(drop=True), y_pred_df], axis=1)

    # 필요한 열만 출력
    result_df = result_df[["park_name", "pre_parking_time", "pred_parking", "cur_parking_time", "cur_parking_new"]]

    # 결과 출력
    result_df=result_df.sort_values(by='pre_parking_time')
    # send_df=result_df.tail(32)
    send_df=result_df
    send_df["pred_parking"]=send_df["pred_parking"].astype(int)
    print(send_df)
    # with connection.cursor() as cursor:
    #     # SQL 쿼리 준비
    #     sql = """
    #     INSERT INTO tb_result (parking_name, pre_parking_time, pred_parking, cur_parking_time, cur_parking_new)
    #     VALUES (%s, %s, %s, %s, %s)
    #     """
        
    #     # 데이터프레임을 반복하면서 삽입
    #     for i, row in send_df.iterrows():
    #         cursor.execute(sql, (
    #             row['park_name'],
    #             row['pre_parking_time'],
    #             row['pred_parking'],
    #             row['cur_parking_time'],
    #             row['cur_parking_new']
    #         ))
        
    #     # 커밋하여 변경사항 저장
    #     connection.commit()
    #     print("Data successfully inserted into tb_pred.")

finally:
    # 연결 종료
    connection.close()

