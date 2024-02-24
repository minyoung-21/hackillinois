from django.db import models

# Create your models here.
class BuildingDetails(models.Model):
    building_name = models.CharField(max_length=200)
    operating_start_hours = models.TimeField(editable=True, blank=True)
    operating_end_hours = models.TimeField(editable=True, blank=True)
    number_of_seats = models.IntegerField()
    outlet_availability = models.BooleanField()
    individual_room_availability = models.BooleanField()
    def __str__(self):
        return self.building_name