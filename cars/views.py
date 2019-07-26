from django.shortcuts import render
from rest_framework import generics

from cars.models import Car
from .serializers import CarDetailSer, CarsSer


# Create your views here.

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSer


class CarsView(generics.ListAPIView):
    serializer_class = CarsSer
    queryset = Car.objects.all()


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSer
    queryset = Car.objects.all()
