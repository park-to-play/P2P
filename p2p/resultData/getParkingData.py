import pymysql
from decouple import config

def getParkingData(target_name):
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
          
          query = """
              SELECT DISTINCT parking_name, pred_parking, pre_parking_time
              FROM tb_result 
              WHERE parking_name = %s
          """
          cursor.execute(query, (target_name))
          rows = cursor.fetchall()
          return rows if rows else []
  except Exception as e:
      return []
  finally:
      connection.close()