from django.shortcuts import render
from rest_framework import generics
from .serializers import CarDetailSer


# Create your views here.

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSer
