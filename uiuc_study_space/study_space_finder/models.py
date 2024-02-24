from django.db import models

# Create your models here.
class BuildingDetails(models.Model):
    building_name = models.CharField(max_length=200)
    operating_hours = models.TimeField()
    number_of_seats = models.IntegerField()
    outlet_availability = models.BooleanField()
    individual_room_availability = models.BooleanField()