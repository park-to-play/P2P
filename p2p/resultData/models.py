from django.db import models

class ParkingResult(models.Model):
    parking_name = models.CharField(max_length=255)
    # 추가 필드를 테이블 구조에 맞게 추가
    location = models.CharField(max_length=255)  # 예시
    available_spaces = models.IntegerField()  # 예시

    class Meta:
        db_table = 'tb_result'  # 기존 MySQL 테이블 이름
