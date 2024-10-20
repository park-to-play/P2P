from rest_framework import serializers
from .models import ParkingResult

class ParkingResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingResult
        fields = ['parking_name', 'location', 'available_spaces']  # 반환할 필드 선택
