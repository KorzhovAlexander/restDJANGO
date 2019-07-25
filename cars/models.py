from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.
class Car(models.Model):
    vin = models.CharField(verbose_name='Vin', db_index=True, unique=True, max_length=24)
    color = models.CharField(verbose_name='Color', db_index=True, max_length=24)
    brand = models.CharField(verbose_name='Brand', db_index=True, max_length=24)
    CAR_TYPES=(
        (1, 'Седан'),
        (2, 'Седан'),
        (3, 'Седан')
    )
    car_type=models.IntegerField(verbose_name='Car_type', choices=CAR_TYPES)
    user=models.ForeignKey(User,verbose_name='User', on_delete=models.CASCADE())

