# myapp/serializers.py
from rest_framework import serializers
from .models import SearchLocation

class SearchLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchLocation
        fields = '__all__'
