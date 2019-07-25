from rest_framework import serializers
from cars.models import Car


class CarDetailSer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
