from django.db import models

# Create your models here.
class ParkingLot(models.Model):
  CURRENT_LAT = models.FloatField(20)
  CURRENT_LNG = models.FloatField(20)

  def __str__(self):
    return self.CURRENT_LNG
