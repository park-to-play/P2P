from rest_framework.generics import ListAPIView
from .models import SearchLocation
from .serializers import SearchLocationSerializer

class SearchLocationListView(ListAPIView):
    queryset = SearchLocation.objects.all()
    serializer_class = SearchLocationSerializer
