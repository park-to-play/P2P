from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ParkingLotSerializer
from .ParkingLotList import find_nearby_parking

class ParkingLotListView(APIView):
    def post(self, request):
        serializer = ParkingLotSerializer(data=request.data)
        if serializer.is_valid():
            CURRENT_LAT = serializer.validated_data.get('CURRENT_LAT')
            CURRENT_LNG = serializer.validated_data.get('CURRENT_LNG')
            result=find_nearby_parking(CURRENT_LAT,CURRENT_LNG)
            return Response(result, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)