from django.urls import path
from .views import SearchLocationListView

urlpatterns = [
    path('search/', SearchLocationListView.as_view(), name='location-list'),
]
