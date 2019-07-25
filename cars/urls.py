from django.contrib import admin
from django.urls import path, include

from cars.views import CarCreateView

urlpatterns = [
    path('create/', CarCreateView.as_view()),
]
