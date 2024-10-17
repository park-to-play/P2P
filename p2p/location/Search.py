from decouple import config
from django.http import JsonResponse
import pymysql

def Search(search_keyword):
  connection = None
  try:
      connection = pymysql.connect(
      host=config("HOST"),
      port=3306,
      user=config("USER_DB"),
      password=config("PASSWORD"),
      database=config("DATABASE"),
      charset=config("CHARSET"),
      )
      
      with connection.cursor() as cursor:
          # tb_address에서 '영등포'가 포함된 주소, 위도, 경도 가져오기
          select_query = """
              SELECT 
                  TRIM(address) AS address, 
                  lat, 
                  lng 
              FROM 
                  tb_address 
              WHERE 
                  address LIKE %s
          """
          # SQL 쿼리에서 '영등포'가 포함된 주소만 가져오도록 설정
          cursor.execute(select_query, ('%' + search_keyword + '%',))
          rows = cursor.fetchall()

          # '서울 영등포구'와 같은 영등포 지역만 필터링
          filtered_rows = {
              
              row for row in rows if "영등포" in row[0]
          }
          

          # 결과 출력
          if filtered_rows:
              return filtered_rows
          else:
              return []
  except Exception as E:
      return f"Search Error with:{E}"

  finally:
      if connection != None:
        connection.close()
