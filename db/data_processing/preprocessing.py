import pandas as pd
from sqlalchemy import create_engine


# 데이터 불러오기

def fetch_table_data(table_name):
    """
    주어진 테이블명을 사용하여 MySQL 데이터베이스에서 데이터를 가져와 DataFrame으로 반환하는 함수.

    Parameters:
        table_name (str): 가져올 테이블의 이름.

    Returns:
        pd.DataFrame: 테이블의 데이터가 담긴 DataFrame.
    """
    # 데이터베이스 연결 설정
    connection_string = 'mysql+pymysql://<사용자명>:<비밀번호>@<호스트>:<포트>/<데이터베이스>?charset=utf8'
    engine = create_engine(connection_string)
    
    try:
        # 데이터 가져오기
        df = pd.read_sql(f"SELECT * FROM {table_name};", engine)
        print(f"'{table_name}' 테이블의 데이터를 성공적으로 불러왔습니다.")
        return df
    except Exception as e:
        print(f"오류 발생: {e}")
        return None
    finally:
        # 엔진 종료
        engine.dispose()



# 주차장 데이터 전처리

def preprocess_parking(df):
    """
    주차장 데이터 전처리 함수 (고정된 주차장 이름 목록 사용)

    Parameters:
        df (pd.DataFrame): 원본 주차장 데이터프레임
    
    Returns:
        pd.DataFrame: 전처리된 주차장 데이터프레임
    """
    # 필터링할 'park_name' 목록 (변경 사항 있을 시 확인 필요)
    filter_park_names = [
        '양화3주차장[양화선착장앞]', '양화1주차장[당산철교 하부]', '양화2주차장[전망카페]', 
        '신한드림리버오피스텔 주차장', '여의도한강3주차장(서강대교남단)', '여의도한강2주차장(마포대교남단)', 
        '파크원 주차장', 'IFC 서울 주차장', '아이엠(im)증권빌딩', 
        '여의도한강4주차장(여의2교-하부파천교)', '당산2동(구)', '롯데마트맥스 영등포점', 
        '당산노외 공영주차장(시)', '영등포제2스포츠센터', '코레일유통 본사 사옥 주차장', 
        '당산근린공원 공영(구)', '영등포구청별관 공영주차장(구)', '우림이비지센타 주차장', 
        '63스퀘어(63빌딩)', '여의도한강공원1주차장(63빌딩앞)', '씨티플라자 주차장', 
        '앵커원', '여의도 사학연금(TP타워)', '영등포구청역 공영주차장(시)', 
        '여의도한강5주차장(성모병원앞)', '금융투자협회', '신길환승(5호선)(구)', 
        '영등포 롯데역사 주차장', '세미콜론문래', '영남 공영주차장(시)', 
        '영등포동제3공영(구)', '홈플러스 영등포점', '문래동공영(구)', 
        '영등포본동제2공영(구)', '도림동 공영주차장(구)', '도림신협본점 옥외주차장', 
        '대림운동장(구)', '대림1동공영(구)'
    ]

    # 주차장 필터링
    filtered_df = df[df['park_name'].isin(filter_park_names)].copy()

    # 'cur_parking_time'의 형식을 '%Y%m%d%H%M'으로 변환할 수 있도록 문자열 정제
    # 초 단위(:SS)제거 'YYYY-MM-DD HH:MM' 형식으로 만듦
    filtered_df['cur_parking_time'] = filtered_df['cur_parking_time'].str.slice(stop=16)

    # 구분 기호(-, :)를 제거
    filtered_df['cur_parking_time'] = filtered_df['cur_parking_time'].str.replace('-', '').str.replace(':', '').str.replace(' ', '')

    # 'cur_parking_time'을 datetime 형식으로 변환 (%Y%m%d%H%M)
    filtered_df['cur_parking_time'] = pd.to_datetime(filtered_df['cur_parking_time'], format='%Y%m%d%H%M', errors='coerce')

    # 'date' 컬럼을 datetime 형식으로 변환
    filtered_df['date'] = pd.to_datetime(filtered_df['date'], errors='coerce')

    # 변환된 'cur_parking_time'에서 변환되지 않은 NaT 값 제거
    filtered_df = filtered_df.dropna(subset=['cur_parking_time'])

    # 시간 및 요일 정보 추출
    filtered_df['hour'] = filtered_df['cur_parking_time'].dt.hour
    filtered_df['day_of_week'] = filtered_df['cur_parking_time'].dt.dayofweek

    # 주말 여부 컬럼 추가 (5: 토요일, 6: 일요일)
    filtered_df['is_weekend'] = filtered_df['day_of_week'] >= 5

    # 범주형 데이터 원 핫 인코딩
    filtered_df = pd.get_dummies(filtered_df, columns=['park_type'])
    filtered_df = pd.get_dummies(filtered_df, columns=['que_status'])

    # 요금 정보 결측치 0으로 대체
    fill_columns = ['park_phone', 'rates', 'day_maximum', 'time_rate', 'add_rates', 'fulltime_monthly']
    filtered_df[fill_columns] = filtered_df[fill_columns].fillna(0)

    return filtered_df



# 기상 데이터 전처리

def preprocess_weather(df):

    # 사용할 컬럼 선택
    selected_features = [
        'address', 'awsStnName', 'awsPty', 'awsTmp', 
        'awsWind', 'lat', 'lon', 'tm'
    ]
    df = df[selected_features]

    # 컬럼명 변경
    rename_columns = {
        'address': '주소',
        'awsStnName': '관측소 이름',
        'awsPty': '강수 형태',
        'awsTmp': '기온',
        'awsWind': '바람속도',
        'lat': 'lat',
        'lon': 'lng',
        'tm': '관측 시간',
    }
    df = df.rename(columns=rename_columns)

    # 영등포구 데이터만 필터링
    df = df[df['주소'].str.startswith('서울특별시 영등포구')]

    # 바람속도 컬럼명 변경
    df.rename(columns={'바람속도': '바람속도m/s'}, inplace=True)

    # 바람속도 데이터 float으로 변경
    df['바람속도m/s'] = pd.to_numeric(df['바람속도m/s'].replace(r'[^0-9.]', '', regex=True), errors='coerce')

    # 강수 형태 데이터 0, 1 값으로 인코딩
    df['강수 형태'] = df['강수 형태'].map({'무': 0, '유': 1}).astype(bool)

    # '관측 시간' 컬럼을 datetime 형식으로 변환
    df['관측 시간'] = pd.to_datetime(df['관측 시간'], format='%Y%m%d%H%M', errors='coerce')

    # 관측소 이름을 단순화
    df['관측소 이름'] = df['관측소 이름'].replace(r'^영등포.*', '영등포', regex=True)

    return df


#def preprocess_gis(df)

#def preprocess_traffic(df)

