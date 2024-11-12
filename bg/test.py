
import joblib
import pandas as pd
import os
import pymysql
import sklearn
import requests
import json
import time
import pytz
from parkingPread import ParkingPrediction
from young import getITS
from datetime import datetime
import threading

# 서울의 타임존 설정
start_time = time.time()
seoul_timezone = pytz.timezone('Asia/Seoul')

# 현재 서울의 시간
seoul_time = datetime.now(seoul_timezone)

current_time = seoul_time.strftime('%Y.%m.%d %H.%M.%S')


loaded_model = joblib.load('./random_forest_model.pkl')

current_file_list = os.listdir('./parking_data')

connection = pymysql.connect(
    # use aws DB connection for get Data from mysql server
)
parking_list = [['양화3주차장[양화선착장앞]', 2],
 ['양화1주차장[당산철교 하부]', 2],
 ['양화2주차장[전망카페]', 2],
 ['신한드림리버오피스텔 주차장', 3],
 ['여의도한강3주차장(서강대교남단)', 2],
 ['여의도한강2주차장(마포대교남단)', 2],
 ['파크원 주차장', 1],
 ['IFC 서울 주차장', 1],
 ['아이엠(im)증권빌딩', 3],
 ['여의도한강4주차장(여의2교-하부파천교)', 2],
 ['당산2동(구)', 3],
 ['롯데마트맥스 영등포점', 1],
 ['당산노외 공영주차장(시)', 3],
 ['영등포제2스포츠센터', 0],
 ['코레일유통 본사 사옥 주차장', 3],
 ['당산근린공원 공영(구)', 2],
 ['여의도한강공원1주차장(63빌딩앞)', 2],
 ['씨티플라자 주차장', 3],
 ['앵커원', 3],
 ['여의도 사학연금(TP타워)', 3],
 ['영등포구청역 공영주차장(시)', 3],
 ['여의도한강5주차장(성모병원앞)', 2],
 ['금융투자협회', 3],
 ['신길환승(5호선)(구)', 3],
 ['영등포 롯데역사 주차장', 1],
 ['세미콜론문래', 3],
 ['영등포동제3공영(구)', 3],
 ['홈플러스 영등포점', 1],
 ['문래동공영(구)', 3],
 ['영등포본동제2공영(구)', 3],
 ['도림동 공영주차장(구)', 3],
 ['대림운동장(구)', 0],
 ['대림1동공영(구)', 3]] 

linkid_list = [['양화3주차장[양화선착장앞]', 1180120000, 50],
['양화3주차장[양화선착장앞]', 1180116501, 50],
['양화3주차장[양화선착장앞]', 1180120300, 50],
['양화3주차장[양화선착장앞]', 1180116502, 50],
['양화3주차장[양화선착장앞]', 1180120400, 30],
['양화3주차장[양화선착장앞]', 1180004202, 80],
['양화1주차장[당산철교 하부]', 1180108100, 30],
['양화1주차장[당산철교 하부]', 1180107400, 80],
['양화1주차장[당산철교 하부]', 1180108000, 30],
['양화1주차장[당산철교 하부]', 1180106800, 30],
['양화2주차장[전망카페]', 1180108100, 30],
['양화2주차장[전망카페]', 1180106900, 30],
['양화2주차장[전망카페]', 1180106300, 30],
['양화2주차장[전망카페]', 1180106400, 30],
['양화2주차장[전망카페]', 1180106800, 30],
['신한드림리버오피스텔 주차장', 1180034901, 50],
['신한드림리버오피스텔 주차장', 1180098900, 30],
['신한드림리버오피스텔 주차장', 1180036101, 40],
['신한드림리버오피스텔 주차장', 1180034500, 60],
['신한드림리버오피스텔 주차장', 1180034801, 50],
['신한드림리버오피스텔 주차장', 1180098800, 30],
['신한드림리버오피스텔 주차장', 1180036001, 40],
['여의도한강3주차장(서강대교남단)', 1180037401, 50],
['여의도한강3주차장(서강대교남단)', 1180034902, 50],
['여의도한강3주차장(서강대교남단)', 1180036102, 40],
['여의도한강3주차장(서강대교남단)', 1180037502, 50],
['여의도한강3주차장(서강대교남단)', 1180035302, 50],
['여의도한강3주차장(서강대교남단)', 1180037501, 50],
['여의도한강2주차장(마포대교남단)', 1180033401, 50],
['여의도한강2주차장(마포대교남단)', 1180030502, 40],
['여의도한강2주차장(마포대교남단)', 1180030900, 50],
['여의도한강2주차장(마포대교남단)', 1180033501, 50],
['여의도한강2주차장(마포대교남단)', 1180094900, 40],
['파크원 주차장', 1180092100, 40],
['파크원 주차장', 1180092000, 40],
['파크원 주차장', 1180095000, 40],
['파크원 주차장', 1180094300, 40],
['파크원 주차장', 1180030403, 40],
['파크원 주차장', 1180030501, 40],
['IFC 서울 주차장', 1180090802, 60],
['IFC 서울 주차장', 1180030203, 50],
['IFC 서울 주차장', 1180090201, 40],
['IFC 서울 주차장', 1180119201, 50],
['IFC 서울 주차장', 1180090102, 40],
['IFC 서울 주차장', 1180125200, 40],
['아이엠(im)증권빌딩', 1180087900, 40],
['아이엠(im)증권빌딩', 1180119202, 60],
['아이엠(im)증권빌딩', 1180090400, 50],
['아이엠(im)증권빌딩', 1180090801, 50],
['아이엠(im)증권빌딩', 1180088000, 40],
['아이엠(im)증권빌딩', 1180090101, 40],
['아이엠(im)증권빌딩', 1180090202, 40],
['아이엠(im)증권빌딩', 1180125100, 40],
['아이엠(im)증권빌딩', 1180125200, 40],
['아이엠(im)증권빌딩', 1180088700, 60],
['여의도한강4주차장(여의2교-하부파천교)', 1180093700, 30],
['여의도한강4주차장(여의2교-하부파천교)', 1180097500, 40],
['여의도한강4주차장(여의2교-하부파천교)', 1180093800, 40],
['당산2동(구)', 1180034203, 50],
['당산2동(구)', 1180094000, 30],
['당산2동(구)', 1180096200, 30],
['당산2동(구)', 1180093900, 30],
['당산2동(구)', 1180034202, 50],
['당산2동(구)', 1180034303, 50],
['당산2동(구)', 1180034302, 50],
['당산2동(구)', 1180096300, 30],
['롯데마트맥스 영등포점', 1180094600, 30],
['롯데마트맥스 영등포점', 1180032002, 50],
['롯데마트맥스 영등포점', 1180032505, 30],
['롯데마트맥스 영등포점', 1180032504, 30],
['롯데마트맥스 영등포점', 1180032102, 50],
['롯데마트맥스 영등포점', 1180032406, 30],
['롯데마트맥스 영등포점', 1180032405, 30],
['롯데마트맥스 영등포점', 1180095800, 30],
['당산노외 공영주차장(시)', 1180031101, 50],
['당산노외 공영주차장(시)', 1180031902, 50],
['당산노외 공영주차장(시)', 1180031002, 50],
['당산노외 공영주차장(시)', 1180031102, 50],
['당산노외 공영주차장(시)', 1180031800, 50],
['당산노외 공영주차장(시)', 1180031001, 50],
['영등포제2스포츠센터', 1180030700, 50],
['영등포제2스포츠센터', 1180032507, 30],
['영등포제2스포츠센터', 1180032506, 30],
['영등포제2스포츠센터', 1180032408, 30],
['영등포제2스포츠센터', 1180031800, 50],
['영등포제2스포츠센터', 1180032407, 30],
['코레일유통 본사 사옥 주차장', 1180030700, 50],
['코레일유통 본사 사옥 주차장', 1180032408, 30],
['코레일유통 본사 사옥 주차장', 1180029000, 50],
['코레일유통 본사 사옥 주차장', 1180029100, 50],
['당산근린공원 공영(구)', 1180031101, 50],
['당산근린공원 공영(구)', 1180028701, 30],
['당산근린공원 공영(구)', 1180093500, 30],
['당산근린공원 공영(구)', 1180028601, 30],
['당산근린공원 공영(구)', 1180093400, 30],
['당산근린공원 공영(구)', 1180031001, 50],
['여의도한강공원1주차장(63빌딩앞)', 1180018705, 50],
['여의도한강공원1주차장(63빌딩앞)', 1180018706, 50],
['여의도한강공원1주차장(63빌딩앞)', 1180073900, 60],
['여의도한강공원1주차장(63빌딩앞)', 1180018704, 50],
['씨티플라자 주차장', 1180090201, 40],
['씨티플라자 주차장', 1180090101, 40],
['씨티플라자 주차장', 1180090102, 40],
['씨티플라자 주차장', 1180090202, 40],
['씨티플라자 주차장', 1180125100, 40],
['앵커원', 1180026702, 50],
['앵커원', 1180030402, 40],
['앵커원', 1180086300, 30],
['앵커원', 1180026602, 50],
['앵커원', 1180030501, 40],
['여의도 사학연금(TP타워)', 1180086800, 40],
['여의도 사학연금(TP타워)', 1180022702, 40],
['여의도 사학연금(TP타워)', 1180082401, 40],
['여의도 사학연금(TP타워)', 1180082600, 40],
['여의도 사학연금(TP타워)', 1180022602, 40],
['여의도 사학연금(TP타워)', 1180082302, 40],
['여의도 사학연금(TP타워)', 1180082700, 40],
['여의도 사학연금(TP타워)', 1180086900, 40],
['영등포구청역 공영주차장(시)', 1180031101, 50],
['영등포구청역 공영주차장(시)', 1180028701, 30],
['영등포구청역 공영주차장(시)', 1180025700, 50],
['영등포구청역 공영주차장(시)', 1180028601, 30],
['영등포구청역 공영주차장(시)', 1180031001, 50],
['여의도한강5주차장(성모병원앞)', 1180018701, 50],
['여의도한강5주차장(성모병원앞)', 1180017701, 50],
['여의도한강5주차장(성모병원앞)', 1180123500, 30],
['여의도한강5주차장(성모병원앞)', 1180017702, 50],
['여의도한강5주차장(성모병원앞)', 1180017603, 50],
['금융투자협회', 1180022901, 50],
['금융투자협회', 1180022801, 50],
['금융투자협회', 1180022802, 50],
['금융투자협회', 1180019103, 50],
['금융투자협회', 1180019002, 50],
['금융투자협회', 1180022902, 50],
['신길환승(5호선)(구)', 1180075100, 50],
['신길환승(5호선)(구)', 1180074400, 50],
['신길환승(5호선)(구)', 1180078700, 50],
['신길환승(5호선)(구)', 1180076300, 50],
['신길환승(5호선)(구)', 1180018503, 50],
['신길환승(5호선)(구)', 1180020601, 50],
['영등포 롯데역사 주차장', 1180018002, 50],
['영등포 롯데역사 주차장', 1180067601, 50],
['영등포 롯데역사 주차장', 1180067602, 60],
['영등포 롯데역사 주차장', 1180000901, 50],
['영등포 롯데역사 주차장', 1180001001, 50],
['세미콜론문래', 1180068700, 60],
['세미콜론문래', 1180069600, 60],
['세미콜론문래', 1180066802, 40],
['세미콜론문래', 1180068500, 40],
['세미콜론문래', 1180068800, 60],
['세미콜론문래', 1180067200, 40],
['세미콜론문래', 1180069700, 60],
['세미콜론문래', 1180069800, 60],
['세미콜론문래', 1180067300, 40],
['영등포동제3공영(구)', 1180016105, 60],
['영등포동제3공영(구)', 1180018901, 50],
['영등포동제3공영(구)', 1180018802, 50],
['영등포동제3공영(구)', 1180127500, 30],
['영등포동제3공영(구)', 1180127600, 30],
['홈플러스 영등포점', 1180017403, 50],
['홈플러스 영등포점', 1180070300, 60],
['홈플러스 영등포점', 1180019701, 30],
['홈플러스 영등포점', 1180017503, 50],
['홈플러스 영등포점', 1180070200, 60],
['홈플러스 영등포점', 1180072100, 30],
['홈플러스 영등포점', 1180072000, 30],
['홈플러스 영등포점', 1180019601, 30],
['문래동공영(구)', 1180068300, 50],
['문래동공영(구)', 1180018303, 30],
['문래동공영(구)', 1180018201, 30],
['문래동공영(구)', 1180018304, 30],
['문래동공영(구)', 1180016800, 50],
['문래동공영(구)', 1180018302, 30],
['문래동공영(구)', 1180018203, 30],
['문래동공영(구)', 1180068200, 50],
['문래동공영(구)', 1180016900, 50],
['영등포본동제2공영(구)', 1180064200, 30],
['영등포본동제2공영(구)', 1180014004, 50],
['영등포본동제2공영(구)', 1180128400, 30],
['영등포본동제2공영(구)', 1180014003, 50],
['영등포본동제2공영(구)', 1180122500, 30],
['영등포본동제2공영(구)', 1180122600, 30],
['영등포본동제2공영(구)', 1180124500, 30],
['영등포본동제2공영(구)', 1180124600, 30],
['영등포본동제2공영(구)', 1180128300, 30],
['도림동 공영주차장(구)', 1180049700, 30],
['도림동 공영주차장(구)', 1180013501, 50],
['도림동 공영주차장(구)', 1180050500, 30],
['도림동 공영주차장(구)', 1180013402, 50],
['도림동 공영주차장(구)', 1180013502, 50],
['도림동 공영주차장(구)', 1180013401, 50],
['도림동 공영주차장(구)', 1180050400, 30],
['대림운동장(구)', 1180130300, 50],
['대림운동장(구)', 1180044300, 50],
['대림운동장(구)', 1180045600, 30],
['대림운동장(구)', 1180045200, 30],
['대림운동장(구)', 1180044000, 50],
['대림1동공영(구)', 1180006802, 50],
['대림1동공영(구)', 1180006601, 50],
['대림1동공영(구)', 1180006902, 30],
['대림1동공영(구)', 1180006700, 50]]

hanriver = ['신한드림리버오피스텔 주차장',
'여의도한강3주차장(서강대교남단)',
'여의도한강2주차장(마포대교남단)',
'파크원 주차장',
'IFC 서울 주차장',
'아이엠(im)증권빌딩',
'여의도한강공원1주차장(63빌딩앞)',
'씨티플라자 주차장',
'앵커원',
'여의도 사학연금(TP타워)',
'여의도한강5주차장(성모병원앞)',
'금융투자협회'] #한강

yeongdongpo = ['양화3주차장[양화선착장앞]',
'양화1주차장[당산철교 하부]',
'양화2주차장[전망카페]',
'여의도한강4주차장(여의2교-하부파천교)',
'당산2동(구)',
'롯데마트맥스 영등포점',
'당산노외 공영주차장(시)',
'영등포제2스포츠센터',
'코레일유통 본사 사옥 주차장',
'당산근린공원 공영(구)',
'영등포구청역 공영주차장(시)',
'신길환승(5호선)(구)',
'영등포 롯데역사 주차장',
'세미콜론문래',
'영등포동제3공영(구)',
'홈플러스 영등포점',
'문래동공영(구)',
'영등포본동제2공영(구)',
'도림동 공영주차장(구)',
'대림운동장(구)',
'대림1동공영(구)'] #영등포

def getParking():
    last_parking_data = os.listdir('./parking_data')
    last_parking_data.sort()  
    last_parking_file=last_parking_data[-1]
    print(last_parking_file)
    df= pd.read_json(f'./parking_data/{last_parking_file}')
    rename_columns = {
        "현재 주차 차량 수":"cur_parking_new",
        "현재 주차 갱신 시간":"cur_parking_time",
        "주차장 이름":"park_name"
    }
    df.rename(columns=rename_columns, inplace=True)
    print(df.loc[df["park_name"] == "여의도 사학연금(TP타워)", "cur_parking_new"])
    df.loc[df["park_name"] == "여의도 사학연금(TP타워)", "cur_parking_new"] -= 494
    df.loc[df["park_name"] == "코레일유통 본사 사옥 주차장", "cur_parking_new"] += 40
    df.loc[df["park_name"] == "당산근린공원 공영(구)", "cur_parking_new"] -= 43
    print(df.loc[df["park_name"] == "여의도 사학연금(TP타워)", "cur_parking_new"])
    return df[["park_name", "cur_parking_new", "cur_parking_time"]]


def getTraffic():
    df = getITS.its_traffic_data()
    df.drop(columns={'roadName', 'roadDrcType', 'linkNo', 'startNodeId', 'endNodeId', 'travelTime'}, inplace=True)
    link_ids = [i[1] for i in linkid_list]
    df['linkId'] = df["linkId"].astype(int)  
    df = df[df['linkId'].isin(link_ids)]
    for park_name, link_id, max_spd in linkid_list:
        # df에서 'linkId'가 현재 link_id와 일치하는 행 필터링
        df.loc[df['linkId'] == link_id, 'park_name'] = park_name
        df.loc[df['linkId'] == link_id, 'max_spd'] = max_spd
    df = df[['park_name', 'linkId', 'speed', 'max_spd',"createdDate"]]  
    df['speed'] = df['speed'].astype(float)  
    df['confusion'] = df['speed'] / df['max_spd']
    # confusion 열의 평균을 주차장 이름 별로 계산
    confusion_df = df.groupby(['park_name', 'createdDate'])['confusion'].mean().reset_index()
    confusion_df.loc[confusion_df['confusion'] >= 1, 'confusion'] = 1.00
    confusion_df['confusion'] = 1 - confusion_df['confusion']
    confusion_df['confusion'] = confusion_df['confusion'].round(2)
    confusion_df['createdDate'] = pd.to_datetime(confusion_df['createdDate'], format='%Y%m%d%H%M%S')
    confusion_df = confusion_df.sort_values(by='createdDate')
    print("confusion_df")
    return confusion_df




def preprocess_weather(weather_df):
    # 사용할 컬럼 선택
    selected_features = [
        'address', 'awsStnName', 'awsPty', 'awsPcpM15', 'awsPcpHr1', 'tm', 'awsTmp', 'awsWs10' , 'awsReh'
    ]
    weather_df = weather_df[selected_features]
    
    # 컬럼명 변경
    rename_columns = {
        'address': '주소',
        'awsTmp' : 'temperature',
        'awsWs10' : '10m/w',
        'awsReh' : 'humidity',
        'awsStnName': '관측소 이름',
        'awsPty': 'now/r',
        'awsPcpM15': '15m/r',
        'awsPcpHr1': '1h/r',
        'tm': '관측 시간',
    }
    weather_df = weather_df.rename(columns=rename_columns)
    
    # 영등포구 데이터만 필터링
    # weather_df=weather_df.dropna()
    weather_df = weather_df[weather_df['주소'].str.startswith('서울특별시 영등포구')]
    
    # 강수 형태 데이터 0, 1 값으로 인코딩
    weather_df['now/r'] = weather_df['now/r'].map({'무': 0, '유': 1}).astype(bool)
    
    # '관측 시간' 컬럼을 datetime 형식으로 변환
    weather_df['관측 시간'] = pd.to_datetime(weather_df['관측 시간'], format='%Y%m%d%H%M', errors='coerce')
    
    # 관측소 이름을 단순화
    weather_df['관측소 이름'] = weather_df['관측소 이름'].replace(r'^영등포.*', '영등포', regex=True)
    
    # '주소' 컬럼 삭제
    weather_df.drop(columns={'주소'}, inplace=True)
    
    # 강수량 여부를 True/False로 변환
    weather_df.loc[weather_df['15m/r'].notna(), '15m/r'] = True
    weather_df.loc[weather_df['15m/r'].isna(), '15m/r'] = False
    weather_df.loc[weather_df['1h/r'].notna(), '1h/r'] = True
    weather_df.loc[weather_df['1h/r'].isna(), '1h/r'] = False
    weather_df = weather_df.sort_values(by='관측 시간')
    weather_df = weather_df.drop_duplicates(subset=['관측소 이름', '관측 시간'])
    return weather_df


def getWeather():
    total_df = pd.DataFrame()
    fix_date = current_time.split(' ')
    for i in [510,418]:
        test_df = pd.DataFrame()
        hour=fix_date[1].split('.')[0]
        mint=fix_date[1].split('.')[1]
        url = f"https://www.weather.go.kr/w/observation/land/aws-obs-data.do?db=MINDB_01M&tm={fix_date[0]}%20{hour}%3A{mint}&stnId={i}&sidoCode=1100000000&sort=&config="
        row_Data=requests.get(url)
        time.sleep(0.1)
        loo=json.loads(row_Data.text)
        row=pd.DataFrame(loo["items"])
        test_df=pd.concat([test_df,row])
        test_df["lat"]=loo["stnInfo"]["lat"]
        test_df["lon"]=loo["stnInfo"]["lon"]
        test_df["awsId"]=loo["stnInfo"]["awsId"]
        total_df = pd.concat([total_df,test_df])
    total_df= preprocess_weather(total_df)
    return total_df


def update_parking_data(parking_df, df):
    merged_df = pd.merge(df, parking_df, on='park_name', suffixes=('', '_new'), how='left')
    
    overlapping_columns = [col for col in parking_df.columns if col in df.columns and col != 'park_name']
    
    # Overwrite the columns in df with the values from parking_df
    for col in overlapping_columns:
        # Replace df's column values with parking_df's column values (suffixed with '_new')
        merged_df[col] = merged_df[f'{col}_new'].combine_first(merged_df[col])
        
        # Drop the temporary '_new' column from the merge
        merged_df.drop(columns=[f'{col}_new'], inplace=True)
    date=current_time.split(' ')[0]
    merged_df['weekday'] = int(date.split('.')[-1]) - 20
    merged_df['holiday'] = 0
    merged_df.drop(columns=["occupancy_rate","temperature", "humidity", "confusion"], axis=1,inplace=True)
    merged_df.rename(columns={"now/r": "now_r", "1h/r": "1h_r", "15m/r": "15m_r", "10m/w": "10m_w"}, inplace=True)
    return merged_df

def update_weather_data(weather_df, df):
    merged_df = pd.merge(df, weather_df, on='park_name', suffixes=('', '_new'), how='left')
    
    merged_df['cur_parking_new'] = merged_df['cur_parking_new_new'].fillna(merged_df['cur_parking_new'])
    
    merged_df.drop(columns=['cur_parking_new_new'], inplace=True)
    return merged_df




def merge(parking_df, weather_df):
    parking_df['cur_parking_time'] = pd.to_datetime(parking_df['cur_parking_time'])
    parking_df['cur_parking_time'] = parking_df['cur_parking_time'].dt.floor('T')
    
    # 'target_time' 생성 (현재 시간에서 20분 전 시간)
    weather_df['관측소 이름'] = weather_df['관측소 이름'].replace(r'^영등포.*', '영등포', regex=True)
    parking_df['target_time'] = parking_df['cur_parking_time']
    
    # weather_df에서 '관측 시간'을 DateTime 형식으로 변환
    weather_df.loc[:, '관측 시간'] = pd.to_datetime(weather_df['관측 시간'])

    # A 리스트의 주차장은 한강, B 리스트의 주차장은 영등포로 매핑
    parking_df['관측소 이름'] = parking_df['park_name'].apply(lambda x: '한강' if x in hanriver else ('영등포' if x in yeongdongpo else None))
    
    # 'target_time'과 '관측소 이름'을 기준으로 parking_df와 weather_df를 병합
    df_merged = pd.merge(parking_df, weather_df, left_on=['관측소 이름', 'target_time'], right_on=['관측소 이름', '관측 시간'], how='left')
    print("df_merged")
    return df_merged[['park_name','cur_parking_time', 'now/r', '15m/r', '10m/w', '1h/r','cur_parking_new']]

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

df=pd.read_csv('./base_df2.csv')
if "Unnamed: 0" in df.columns:
    df.drop('Unnamed: 0',axis=1,inplace=True)
if "Unnamed: 0.1" in df.columns:
    df.drop('Unnamed: 0.1',axis=1,inplace=True)



def insert_dataframe_to_table(df, table_name):
    # DB에 삽입할 SQL 쿼리 생성
    df = df.dropna()
    cols = ",".join([f"`{i}`" for i in df.columns.tolist()])  
    sql = f"INSERT INTO {table_name} ({cols}) VALUES ({', '.join(['%s'] * len(df.columns))})"
    
    # 연결 객체를 밖에서 받아오는 방식으로 가정
    connection = pymysql.connect(
        # use aws DB connection for get Data from mysql server
    )
    if connection.open:  # 커넥션이 열려 있는지 확인
        print("DB 연결 성공!")
    else:
        print("DB 연결 실패!")
        return  # 연결이 실패하면 함수 종료
    with connection.cursor() as cursor:
        # 데이터프레임을 튜플 리스트로 변환
        data = [tuple(row) for row in df.values]
        # executemany로 배치 삽입
        cursor.executemany(sql, data)  
        connection.commit()  # 모든 데이터 삽입 후 커밋
    connection.close()
    print("Data inserted successfully!")

def get_tb_tf():
    sql = "SELECT * FROM tb_tf"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        columns = [col[0] for col in cursor.description]  # 컬럼 이름 추출
    df = pd.DataFrame(result, columns=columns)  # DataFrame으로 변환
    return df
            # 현재 파일 리스트 업데이트
db_config = {
        'host': '15.165.195.216',
        'port': 3306,
        'database': 'p2p',
        'user': 'tester',
        'password': 'park_to_play_db',
        'charset': 'utf8'
        }

# while True:
weather_df = getWeather()
parking_df = getParking()
traffic_df = getTraffic()
m1_df = merge(parking_df, weather_df)
m2_df = update_parking_data(m1_df, df)
tb_tf = m2_df.merge(traffic_df[['park_name', 'confusion']], on='park_name', how='left')
tb_tf=tb_tf.drop(columns=['cur_parking_new'])
if "Unnamed: 0.1" in tb_tf.columns:
    tb_tf.drop('Unnamed: 0.1',axis=1,inplace=True)
print("here", tb_tf)
insert_dataframe_to_table(tb_tf, 'tb_tf')

while True:
    try:
        check_file_list = os.listdir('./parking_data')  # 파일 목록 확인
        print("Start time:", start_time)
        
        # # 새로운 파일이 있는지 확인
        # if len(check_file_list) > len(current_file_list):
        print("New files detected, processing start.")
        print(f"New file count: {len(check_file_list)} | Old file count: {len(current_file_list)}")
        current_file_list = check_file_list
        print(f"change: {len(check_file_list)} | Old file count: {len(current_file_list)}")
        weather_df = getWeather()
        parking_df = getParking()
        traffic_df = getTraffic()
        m1_df = merge(parking_df, weather_df)
        m2_df = update_parking_data(m1_df, df)
        #교통 통합
        tf_pred= m2_df.merge(traffic_df[['park_name', 'confusion']], on='park_name', how='left')

        # 데이터프레임을 테이블에 삽입
        past_df=get_tb_tf()

        # 먼저 두 데이터프레임을 park_name 기준으로 병합합니다.
        merged_df = past_df.merge(tf_pred[['park_name', 'cur_parking_new']], on='park_name', how='left')

        # 병합된 데이터프레임에서 cur_parking_new 값을 past_tf에 넣습니다.
                
        tf_pred = tf_pred.drop(columns=['cur_parking_new'])
        connection = pymysql.connect(
            # use aws DB connection for get Data from mysql server
        )
        if "Unnamed: 0.1" in tf_pred.columns:
            tf_pred.drop('Unnamed: 0.1',axis=1,inplace=True)
        if connection.open:  # 커넥션이 열려 있는지 확인
            print("DB 연결 성공!")
        else:
            print("DB 연결 실패!")
        with connection.cursor() as cursor:
            # TRUNCATE 명령 실행
            
            truncate_query = "DELETE FROM tb_tf WHERE confusion < 2;"
            cursor.execute(truncate_query)
            connection.commit()   
        
        # 변경사항 커밋
        print("테이블 tb_tf의 데이터가 모두 삭제되었습니다.")
        tf_pred = tf_pred.drop_duplicates()
        insert_dataframe_to_table(tf_pred, 'tb_tf')
        insert_dataframe_to_table(merged_df, 'tb_tf_shift')
        print("m2_df inserted into tb_tf_shift, tb_tf")

        parking_prediction = ParkingPrediction(db_config=db_config)
        parking_prediction.run()
        # print("Sleeping for 7 minutes.")
        # time.sleep(60)
        # print("Waking up and checking again.")

    except FileNotFoundError as fnf_error:
        print(f"File not found error: {fnf_error}")
        # break

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # break
    break
connection.close()