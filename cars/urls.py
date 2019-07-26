from django.contrib import admin
from django.urls import path, include

from cars.views import CarCreateView, CarsView, CarDetailView

urlpatterns = [
    path('create/', CarCreateView.as_view()),
    path('list/', CarsView.as_view()),
    path('car-<int:pk>/', CarDetailView.as_view()),
]
