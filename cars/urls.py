from django.urls import path
from .views import CarListCreateAPIView

urlpatterns = [
    path('cars/', CarListCreateAPIView.as_view(), name='car-list-create'),
]