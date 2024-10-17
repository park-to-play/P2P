from django.db import models

# Create your models here.
class SearchLocation(models.Model):
  location = models.CharField(max_length=100)

  def __str__(self):
    return self.location