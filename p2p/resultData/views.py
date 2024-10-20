from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .getParkingData import getParkingData
from .models import ParkingResult

class ParkingResultView(APIView):
    def get(self, request):
        parking_name = request.query_params.get('parking_name', None)
        if parking_name:
            try:
                data=getParkingData(parking_name)
                return Response(data, status=status.HTTP_200_OK)
            except ParkingResult.DoesNotExist:
                return Response({"error": "Parking result not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": "Parking name parameter is missing."}, status=status.HTTP_400_BAD_REQUEST)
