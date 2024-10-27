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
            ORDER BY pre_parking_time DESC
            LIMIT 1
        """
        cursor.execute(query, (target_name))
        rows = cursor.fetchall()
        query = """
            SELECT park_name, cur_parking_new, cur_parking_time
            FROM tb_tf_shift 
            WHERE park_name = %s
            ORDER BY cur_parking_time DESC
            LIMIT 20
        """
        cursor.execute(query, (target_name))
        rows_2 = cursor.fetchall()
        combined_rows = [
                (parking_name, pred_parking, pre_parking_time) for parking_name, pred_parking, pre_parking_time in rows
            ] + [
                (park_name, cur_parking_new, cur_parking_time) for park_name, cur_parking_new, cur_parking_time in rows_2
            ]
        return combined_rows if combined_rows else []

  except Exception as e:
      print("Error: ",e)
      return []
  finally:
      connection.close()