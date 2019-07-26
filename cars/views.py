from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cars.models import Car
from .serializers import CarDetailSer, CarsSer
from .permissions import IsOwnerOrReadOnly


# Create your views here.

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSer

    def post(self, request, *args, **kwargs):
        print(request.data)
        return Response


class CarsView(generics.ListAPIView):
    serializer_class = CarsSer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated, )


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
