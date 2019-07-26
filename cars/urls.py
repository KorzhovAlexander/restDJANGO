from django.contrib import admin
from django.urls import path, include

from cars.views import CarCreateView, CarsView

urlpatterns = [
    path('create/', CarCreateView.as_view()),
    path('list/', CarsView.as_view()),

]
