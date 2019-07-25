from django.db import models

# Create your models here.
class Car(models.Model):
    vin = models.CharField(verbose_name='Vin',db_index=True, unique=True, max_length=24)

