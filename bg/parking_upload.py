import pandas as pd
import os
import json
import pymysql
import time
from datetime import datetime
import pytz

# MySQL 연결 설정
connection = pymysql.connect(
    # use aws DB connection for get Data from mysql server
)

# JSON 파일 목록과 CSV 파일 읽기
json_list = os.listdir("./parking_data")
df = pd.read_csv("./upload_base/parking_data_base.csv")
with open(f"./upload_base/base.json",'r',encoding='UTF-8') as f:
  json_data = json.load(f)
raw_df =pd.DataFrame(json_data)
start_time = time.time()

def emptyString(target):
  try:
    if target == "":
        return None
    elif "원" in str(target):
      return int(target.strip().split("원")[0])
    else:
      return target
  except:
    return None

def clean_data(data):
    try:
      cleaned_data = {}
      
      #### 필수 데이터 ####
      
      cleaned_data['lat'] = float(data['lat']) 
      cleaned_data['lng'] = float(data['lng']) 
      cleaned_data['capacity'] = int(data['capacity']) 
      cleaned_data['cur_parking'] = int(data['cur_parking']) 
      cleaned_data['available_parking'] = int(data['available_parking']) 
      
      cleaned_data['park_name'] = data['park_name']
      cleaned_data['park_address'] = data['park_address']
      
      cleaned_data['park_type'] = data['park_type']
      if data['rates'].isdigit():
        cleaned_data['rates'] = int(data['rates'].strip())
      else:
        # 우이동 공영주차장(시) 때매!!!
        # 공유) 장승배기로B(구) 아오
        cleaned_data['rates'] = emptyString(data['rates'].strip().split("원")[0])
      
      ################################################
      
      #### 옵션 데이터 ####
      cleaned_data['count'] = emptyString(data['count']) 
      cleaned_data['date'] = emptyString(data['date']) 
      cleaned_data['add_rates'] = emptyString(data['add_rates']) 
      cleaned_data['fulltime_monthly'] = emptyString(data['fulltime_monthly'])
      cleaned_data['cur_parking_time'] = data['cur_parking_time'].strip()
      cleaned_data['weekday_begin_time'] = emptyString(data['weekday_begin_time'])
      cleaned_data['weekday_end_time'] = emptyString(data['weekday_end_time'])
      cleaned_data['time_rate'] = emptyString(data['time_rate'].split("분")[0])
      cleaned_data['weekend_begin_time'] = emptyString(data['weekend_begin_time'])
      cleaned_data['day_maximum'] = emptyString(data['day_maximum']) 
      cleaned_data['weekend_end_time'] = emptyString(data['weekend_end_time'])
      cleaned_data['holiday_begin_time'] = emptyString(data['holiday_begin_time'])
      cleaned_data['holiday_end_time'] = emptyString(data['holiday_end_time'])
      cleaned_data['park_phone'] = data['park_phone'].strip()
      cleaned_data['que_status'] = data['que_status']
      ################################################
      return cleaned_data
    except Exception as e:
       print("clean Error data: ", data)
       print(f"Error in cleaning {e}, {cleaned_data}")

# 주차장 데이터를 변환하는 함수
def transform_parking_data(data):
    # Create a dictionary with default values as None
    transformed_data = {
        "park_name": None,
        "park_address": None,
        "lat": None,
        "lng": None,
        "park_type": None,
        "capacity": None,
        "cur_parking": None,
        "available_parking": None,
        "rates": None,
        "add_rates": None,
        "time_rate": None,
        "fulltime_monthly": None,
        "day_maximum": None,
        "cur_parking_time": None,
        "weekday_begin_time": None,
        "weekday_end_time": None,
        "weekend_begin_time": None,
        "weekend_end_time": None,
        "holiday_begin_time": None,
        "holiday_end_time": None,
        "park_phone": None,
        "que_status": None,
        "count": None,
        "date": None
    }
    if "주차장 이름" in data:  
      transformed_data["park_name"] = data.get("주차장 이름")
      transformed_data["park_address"] = data.get("주소")
      transformed_data["lat"] = data.get("위치 정보", [[None, None]])[0][0]
      transformed_data["lng"] = data.get("위치 정보", [[None, None]])[0][1]
      transformed_data["park_type"] = data.get("주차 타입")
      transformed_data["capacity"] = data.get("전체 주차 면")
      transformed_data["cur_parking"] = data.get("현재 주차 차량 수")
      transformed_data["available_parking"] = data.get("주차 가능 면")
      transformed_data["rates"] = data.get("요금")
      transformed_data["add_rates"] = data.get("추가 요금")
      transformed_data["time_rate"] = data.get("요금 부과 기준")
      transformed_data["fulltime_monthly"] = data.get("정기권 요금")
      transformed_data["day_maximum"] = data.get("일일 최대 요금")
      transformed_data["cur_parking_time"] = data.get("현재 주차 갱신 시간")
      transformed_data["weekday_begin_time"] = data.get("평일 운영 시간", None).split(" ~ ")[0]
      transformed_data["weekday_end_time"] = data.get("평일 운영 시간", None).split(" ~ ")[1]
      transformed_data["weekend_begin_time"] = data.get("주말 운영 시간", None).split(" ~ ")[0]
      transformed_data["weekend_end_time"] = data.get("주말 운영 시간", None).split(" ~ ")[1]
      transformed_data["holiday_begin_time"] = data.get("공휴일 운영 시간", None).split(" ~ ")[0]
      transformed_data["holiday_end_time"] = data.get("공휴일 운영 시간", None).split(" ~ ")[1]
      transformed_data["park_phone"] = data.get("전화번호")
      transformed_data["que_status"] = data.get("연계 상태")
      transformed_data["count"] = data.get("count")
      transformed_data["date"] = data.get("date")
    else:  # English format (demo)
      try:
        matching_rows = raw_df[raw_df["주소"] == data.get("address")]
        if matching_rows.empty:
          matching_rows = raw_df[raw_df["주차장 이름"] == data.get("parking_name")]
        matching_index=matching_rows.index[0]
        transformed_data["park_name"] = data.get("parking_name")
        transformed_data["park_address"] = data.get("address")
        transformed_data["lat"] = data.get("lat")
        transformed_data["lng"] = data.get("lng")
        transformed_data["park_type"] = raw_df.at[matching_index, "주차 타입"]  # Static Value
        transformed_data["capacity"] = data.get("capacity")
        transformed_data["cur_parking"] = data.get("cur_parking")
        transformed_data["available_parking"] = int(data.get("capacity")) - int(data.get("cur_parking"))
        transformed_data["rates"] = raw_df.at[matching_index, "요금"] # Static Value
        transformed_data["add_rates"] = raw_df.at[matching_index, "추가 요금"].replace('원', '')  # Static Value
        transformed_data["time_rate"] = raw_df.at[matching_index, "요금 부과 기준"] # Static Value
        transformed_data["fulltime_monthly"] = raw_df.at[matching_index, "정기권 요금"].replace('원', '') # Static Value
        transformed_data["day_maximum"] = data.get("day_maximum")
        transformed_data["cur_parking_time"] = data.get("cur_parking_time")
        transformed_data["weekday_begin_time"] = raw_df.at[matching_index,"평일 운영 시간"].split(" ~ ")[0] # Static Value
        transformed_data["weekday_end_time"] = raw_df.at[matching_index,"평일 운영 시간"].split(" ~ ")[1] # Static Value
        transformed_data["weekend_begin_time"] = raw_df.at[matching_index,"주말 운영 시간"].split(" ~ ")[0] # Static Value
        transformed_data["weekend_end_time"] = raw_df.at[matching_index,"주말 운영 시간"].split(" ~ ")[1] # Static Value
        transformed_data["holiday_begin_time"] = raw_df.at[matching_index,"공휴일 운영 시간"].split(" ~ ")[0] # Static Value
        transformed_data["holiday_end_time"] = raw_df.at[matching_index,"공휴일 운영 시간"].split(" ~ ")[1] # Static Value
        transformed_data["park_phone"] = data.get("phone")
        transformed_data["que_status"] = raw_df.at[matching_index,"연계 상태"] # Static Value
        transformed_data["count"] = data.get("count")
        transformed_data["date"] = data.get("date") 
      except Exception as e:
        # 최근 데이터에 주차장 명, 주차장 주소가 동일한게 없으면 None으로 입력 -> 이후 찾아서 수기로 넣어야할듯
        transformed_data["park_name"] = data.get("parking_name")
        transformed_data["park_address"] = data.get("address")
        transformed_data["lat"] = data.get("lat")
        transformed_data["lng"] = data.get("lng")
        transformed_data["park_type"] = None
        transformed_data["capacity"] = data.get("capacity")
        transformed_data["cur_parking"] = data.get("cur_parking")
        transformed_data["available_parking"] = int(data.get("capacity")) - int(data.get("cur_parking"))
        transformed_data["rates"] = ""
        transformed_data["add_rates"] = None
        transformed_data["time_rate"] = ""
        transformed_data["fulltime_monthly"] = None
        transformed_data["day_maximum"] = data.get("day_maximum")
        transformed_data["cur_parking_time"] = data.get("cur_parking_time")
        transformed_data["weekday_begin_time"] = None
        transformed_data["weekday_end_time"] = None
        transformed_data["weekend_begin_time"] = None
        transformed_data["weekend_end_time"] = None
        transformed_data["holiday_begin_time"] = None
        transformed_data["holiday_end_time"] = None
        transformed_data["park_phone"] = data.get("phone")
        transformed_data["que_status"] = None
        transformed_data["count"] = data.get("count")
        transformed_data["date"] = data.get("date") 
    return transformed_data

# 메인 루프: 1시간마다 주차장 데이터를 업데이트
file_set = set()
# while True:
new_data_list = []

for file_name in json_list:
    if file_name in file_set:
        continue

    # JSON 데이터 읽기
    with open(f"./parking_data/{file_name}", 'r', encoding='UTF-8') as f:
        json_data = json.load(f)

    for entry in json_data:
      if "address" in entry.keys():
        if entry["address"] in df["주소"].values:
            matching_index = df[df["주소"] == entry["address"]].index[0]
            entry["lat"] = df.at[matching_index, "위도"]
            entry["lng"] = df.at[matching_index, "경도"]
        elif entry["parking_name"] in df["주차장 이름"].values:
            matching_index = df[df["주차장 이름"] == entry["parking_name"]].index[0]
            entry["lat"] = df.at[matching_index, "위도"]
            entry["lng"] = df.at[matching_index, "경도"]
        else:
            print(f"Error_KR: Address or parking name not found in base data for {entry}")
            break
      else:
        if entry["주소"] in df["주소"].values:
            matching_index = df[df["주소"] == entry["주소"]].index[0]
            entry["위도"] = df.at[matching_index, "위도"]
            entry["경도"] = df.at[matching_index, "경도"]
        elif entry["주차장 이름"] in df["주차장 이름"].values:
            matching_index = df[df["주차장 이름"] == entry["주차장 이름"]].index[0]
            entry["위도"] = df.at[matching_index, "위도"]
            entry["경도"] = df.at[matching_index, "경도"]
        else:
            print(f"Error_EN: Address or parking name not found in base data for {entry}")
            break

        # 변환된 데이터 추가
        new_data = transform_parking_data(entry)
        new_data_list.append(new_data)
        file_set.add(file_name)


try:
    print(len(new_data_list))
    for data in new_data_list:  # 데이터 1개만 처리
        cleaned_data = clean_data(data)
        # fixme -> KST로 바꿀것
        utc = pytz.utc
        kst = pytz.timezone('Asia/Seoul')
        cleaned_data['cur_parking_time'] = datetime.strptime(cleaned_data['cur_parking_time'], '%Y-%m-%d %H:%M:%S')
        cleaned_data['date'] = datetime.fromtimestamp(cleaned_data['date'])
        cleaned_data['date'] = utc.localize(cleaned_data['date']).astimezone(kst)
        cleaned_data['date'] = cleaned_data['date'].replace(tzinfo=None)
        with connection.cursor() as cursor:  # 커서 열기
            sql = """
                  INSERT INTO tb_parking (
                      park_name, park_address, lat, lng, park_type, capacity, cur_parking,
                      available_parking, rates, add_rates, time_rate, fulltime_monthly,
                      day_maximum, cur_parking_time, weekday_begin_time, weekday_end_time,
                      weekend_begin_time, weekend_end_time, holiday_begin_time, holiday_end_time,
                      park_phone, que_status, count, date
                  ) VALUES (
                      %(park_name)s, %(park_address)s, %(lat)s, %(lng)s, %(park_type)s, %(capacity)s, %(cur_parking)s,
                      %(available_parking)s, %(rates)s, %(add_rates)s, %(time_rate)s, %(fulltime_monthly)s,
                      %(day_maximum)s, %(cur_parking_time)s, %(weekday_begin_time)s, %(weekday_end_time)s,
                      %(weekend_begin_time)s, %(weekend_end_time)s, %(holiday_begin_time)s, %(holiday_end_time)s,
                      %(park_phone)s, %(que_status)s, %(count)s, %(date)s
                  )
                  """
            cursor.execute(sql, cleaned_data)  # SQL 실행은 커서가 열려 있을 때 해야 함
        connection.commit()  # 커서 블록이 끝난 후 commit
except Exception as e:
    print(f"Error on upload: {e} {file_name} \n {cleaned_data}")
finally:
    connection.close() 
    print(time.time()-start_time)