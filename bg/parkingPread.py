import joblib
import pandas as pd
import pymysql
import pytz
from datetime import datetime
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def round_minute(dt):
    minute = dt.minute
    if 0 <= minute < 20:
        return dt.replace(minute=0, second=0)
    elif 20 <= minute < 40:
        return dt.replace(minute=20, second=0)
    else:
        return dt.replace(minute=40, second=0)


def get_confusion(row, traffic_df):
    row['cur_parking_time'] = pd.to_datetime(row['cur_parking_time'])
    traffic_df['createdDate'] = pd.to_datetime(traffic_df['createdDate'])

    matched_traffic = traffic_df[
        (traffic_df['park_name'] == row['park_name']) & 
        (row['cur_parking_time'] - pd.Timedelta(minutes=25) <= traffic_df['createdDate']) & 
        (traffic_df['createdDate'] <= row['cur_parking_time'] - pd.Timedelta(minutes=5))
    ]

    if not matched_traffic.empty:
        return matched_traffic['confusion'].values[0]
    else:
        return None


class ParkingPrediction:
    
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = pymysql.connect(**db_config)
        self.scaler = StandardScaler()
        self.null_target = ['weekday_1', 'weekday_2', 'weekday_3', 'weekday_4', 'weekday_5', 'weekday_6',
                            'hour_1', 'hour_2', 'hour_3', 'hour_4', 'hour_5', 'hour_6', 'hour_7', 'hour_8',
                            'hour_9', 'hour_10', 'hour_11', 'hour_12', 'hour_13', 'hour_14', 'hour_15',
                            'hour_16', 'hour_17', 'hour_18', 'hour_19', 'hour_20', 'hour_21', 'hour_22', 
                            'hour_23', 'minute_20', 'minute_40', "park_name_영등포 롯데역사 주차장"]
    # ******************수정 필요*********************
    def load_data(self):
        query_tb_df = "SELECT * FROM tb_tf"
        try:
            with self.connection.cursor() as cursor:
                df = pd.read_sql(query_tb_df, self.connection)  # 연결은 open 상태에서 사용
            return df
        except Exception as e:
            print(f"Error while loading data: {e}")
            return None  # 오류 발생 시 None 반환
    
    def preprocess_data(self, df):
        #park_weather_df['confusion'] = park_weather_df.apply(get_confusion, axis=1, traffic_df=traffic_df)
        #park_weather_df.drop(columns=["10m_w"])
        #total_df = tf.tail(32)
        df.rename(columns={
            '10m_w': '10m/w',
            '15m_r': '15m/r',
            '1h_r': '1h/r',
        }, inplace=True)
        
        df['cur_parking_time'] = pd.to_datetime(df['cur_parking_time'])
        df = df[df['cur_parking_time'].dt.date != pd.to_datetime('2024-10-05').date()]
        df['cur_parking_time'] = df['cur_parking_time'].apply(round_minute)

        #df = df.sort_values(by='cur_parking_time')
        df['hour'] = df['cur_parking_time'].dt.hour
        df['minute'] = df['cur_parking_time'].dt.minute
        df['purpose'] = df['purpose'].astype('float')
        df = pd.get_dummies(df, columns=['park_name', 'purpose', 'park_type', 'weekday', 'hour', 'minute'], drop_first=True)
        for col in ['weekday_0', 'hour_0', 'minute_0']:
            if col in df.columns:
                df.drop([col], axis=1, inplace=True)

        df.rename(columns={'now_r': 'now/r'}, inplace=True)
        df.drop(['cur_parking_time', 'time_rate'], axis=1, inplace=True)

        features_to_scale = ['capacity', 'rates', 'add_rates', '10m/w']
        df[features_to_scale] = self.scaler.fit_transform(df[features_to_scale])

        for col in self.null_target:
            if col not in df.columns:
                df[col] = False
        return df

    def predict(self, df, one_df):
        query_tb_shift = "SELECT * FROM tb_tf_shift"
        
        try:
            with self.connection.cursor() as cursor:
                tf = pd.read_sql(query_tb_shift, self.connection)
            
            tf.rename(columns={
                '10m_w': '10m/w',
                '15m_r': '15m/r',
                '1h_r': '1h/r',
                'now_r': 'now/r'
            }, inplace=True)
            
            # 'cur_parking_time'을 datetime 형식으로 변환
            tf['cur_parking_time'] = pd.to_datetime(tf['cur_parking_time'])

            # 여의도에서 가장 큰 축제인 불꽃축제가 열린 날은 주차장 데이터가 이상치가 나왔기 때문에 제외
            tf = tf[tf['cur_parking_time'].dt.date != pd.to_datetime('2024-10-05').date()]

            # 시간을 20분 단위로 반올림
            def round_minute(dt):
                minute = dt.minute
                if 0 <= minute < 20:
                    return dt.replace(minute=0, second=0)
                elif 20 <= minute < 40:
                    return dt.replace(minute=20, second=0)
                else:
                    return dt.replace(minute=40, second=0)

            tf['cur_parking_time'] = tf['cur_parking_time'].apply(round_minute)

            # cur_parking_time 열을 기준으로 시간별로 정렬
            tf = tf.sort_values(by='cur_parking_time')

            # 새로운 열 추가: weekday, hour, minute
            tf['hour'] = tf['cur_parking_time'].dt.hour
            tf['minute'] = tf['cur_parking_time'].dt.minute
            tf['purpose'] = tf['purpose'].astype('float')

            # 수치형 변수들 스케일링을 통한 정규화
            scaler = StandardScaler()
            features_to_scale = ['capacity', 'rates', 'add_rates', '10m/w']
            print("features_to_scale: ", tf[features_to_scale])
            tf[features_to_scale] = scaler.fit_transform(tf[features_to_scale])
            
            # 목적 변수 및 피처 설정
            X = tf.drop(columns=['cur_parking_new', 'cur_parking_time', 'time_rate'])
            y = tf['cur_parking_new']
            print("y nan check",y.isna().sum())
            # 범주형 데이터 원-핫 인코딩
            X = pd.get_dummies(X, columns=['park_name', 'park_type', 'weekday', 'hour', 'minute', 'purpose'], drop_first=True)

            # 데이터 분할
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # 모델 생성
            model = RandomForestRegressor(n_estimators=200, random_state=42)
            model.fit(X_train, y_train)

            # 입력 데이터에 맞게 피처 선택
            df = df[model.feature_names_in_]
            one_df['pred_parking'] = np.round(model.predict(df))
            
            return one_df[['park_name', 'pred_parking']]
        
        except Exception as e:
            print(f"Error while predicting: {e}")
            return None  # 오류 발생 시 None 반환
        

    def save_results(self, result_df):
        send_df = result_df.sort_values(by='pre_parking_time')
        send_df["pred_parking"] = send_df["pred_parking"].astype(int)

        sql = """
        INSERT INTO tb_result (parking_name, pre_parking_time, pred_parking)
        VALUES (%s, %s, %s)
        """
        with self.connection.cursor() as cursor:
            for _, row in send_df.iterrows():
                cursor.execute(sql, (
                    row['park_name'],
                    row['pre_parking_time'],
                    row['pred_parking'],
                ))
            self.connection.commit()

    def run(self):
        try:
            df = self.load_data()
            one_df = df.copy()
            df = self.preprocess_data(df)
            y_pred_df = self.predict(df, one_df.copy())
            merged_df = one_df.merge(y_pred_df[['park_name', 'pred_parking']], on='park_name', how='left')
            one_df['pred_parking'] = merged_df['pred_parking']   
            one_df["pre_parking_time"] = one_df["cur_parking_time"] + pd.to_timedelta(20, unit='m')
            result_df = one_df
            result_df = result_df[["park_name", "pre_parking_time", "pred_parking"]]
            print(result_df)
            self.save_results(result_df)

        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
        finally:
            self.connection.close()


# # 실행 예시
# db_config = {
#     'host': '15.165.195.216',
#     'port': 3306,
#     'database': 'p2p',
#     'user': 'tester',
#     'password': 'park_to_play_db',
#     'charset': 'utf8'
# }

# parking_prediction = ParkingPrediction(db_config=db_config)
# parking_prediction.run()
