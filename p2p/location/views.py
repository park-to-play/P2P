from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SearchLocation
from .serializers import SearchLocationSerializer
from .Search import Search

class SearchLocationListView(APIView):
    def post(self, request):
        serializer = SearchLocationSerializer(data=request.data)
        if serializer.is_valid():
            location = serializer.validated_data.get('location')
            result=Search(location)
            return Response(result, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)