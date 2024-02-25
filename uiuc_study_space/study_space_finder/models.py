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
# import the standard Django Model
# from built-in library
from django.db import models

from osm_field.fields import LatitudeField, LongitudeField, OSMField
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.title


class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    
class MyModel(models.Model):
    location = OSMField(lat_field='latitude', lon_field='longitude')
    latitude = LatitudeField()
    longitude = LongitudeField()
from django import forms
class MyModelForm(forms.ModelForm):

    class Meta:
        fields = ('location', 'latitude', 'longitude', )
        model = MyModel
from django.db import models
from django_google_maps import fields as map_fields

class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
from django.db import models

from django_google_maps.fields import AddressField, GeoLocationField


