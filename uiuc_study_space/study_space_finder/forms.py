from django import forms
from .admin import SampleModel
from django_google_maps.widgets import GoogleMapsAddressWidget


class SampleForm(forms.ModelForm):

    class Meta(object):
        model = SampleModel
        fields = ['address', 'geolocation']
        widgets = {
            "address": GoogleMapsAddressWidget,
        }
