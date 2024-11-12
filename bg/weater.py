import pandas as pd
import pymysql
import time
import numpy as np
# MySQL 연결 설정
start_time = time.time()
connection = pymysql.connect(
    # use aws DB connection for get Data from mysql server
)


df = pd.read_csv("./weather/wb_fin.csv")
df = df.drop(columns=["Unnamed: 0"])
df = df.replace({np.nan: None})
df = df.replace({'-': None})
print(max(df["awsUpdated"]))
print(min(df["awsUpdated"]))
# SQL Insert 쿼리
insert_query = """
INSERT INTO tb_weather (
    dongCode, address, windUnit, x, y, awsStnId, awsUpdated, awsStnName, awsStnNameEng, awsAddr, awsAddrEng, awsAltitude, 
    awsPty, awsPcpM15, awsPcpHr1, awsPcpHr12, awsPcpDay, awsTmp, awsChillTmp, awsWind, awsWindEng, awsWs10, awsWd10, awsWs1, 
    awsWd1, awsWss, awsWds, awsPa, awsPs, awsTd, awsReh, lat, lon, awsTaMin, awsTaMax, awsWssMax, awsWsMax, tm, fullTm, 
    hmTm, distance, awsSp, awsSpCode, awsSpColorCode, awsTroblKnd, altIndex, awsId
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
"""

# 데이터를 튜플 리스트로 변환
data = [tuple(row) for row in df.values]
print(len(df.columns))
print(df.columns)

# 데이터베이스에 데이터 삽입
print("input start")
with connection.cursor() as cursor:
    cursor.executemany(insert_query, data)
    connection.commit()

# 연결 종료
connection.close()

print("End of input dada: ",time.time() - start_time)
