from django.urls import path
from .views import ParkingLotListView

urlpatterns = [
    path('lot/', ParkingLotListView.as_view(), name='parkinglot-list'),
]
