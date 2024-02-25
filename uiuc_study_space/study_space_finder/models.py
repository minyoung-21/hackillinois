from django.db import models

# Create your models here.
class RoomDetails(models.Model):
    room_name = models.CharField(max_length=200)
    building_name = models.CharField(max_length=200)
    floor_number = models.IntegerField(default=0)
    operating_start_hours = models.TimeField(editable=True, blank=True)
    operating_end_hours = models.TimeField(editable=True, blank=True)
    number_of_seats = models.IntegerField()
    outlet_availability = models.BooleanField(default=False)
    tables_availability = models.BooleanField(default=False)
    open_space_availability = models.BooleanField(default=False)
    coordinate_latitude = models.DecimalField(max_digits=9, decimal_places=7, default=0.0)
    coordinate_longitude = models.DecimalField(max_digits=9, decimal_places=7, default=0.0)
    photo = models.ImageField(blank=True, null=True)
    def __str__(self):
        return self.room_name