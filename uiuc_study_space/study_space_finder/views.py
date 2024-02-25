from django.shortcuts import render, get_object_or_404
from .models import BuildingDetails
from .utils import get_live_forecast
from models import Building
building_names = [building.name for building in Building.query.all()]
set_building_names = set(building_names)
building_data = get_live_forecast(set_building_names)

def list_view(request):
    return render(request, "list.html", {"buildings": BuildingDetails.objects.all()})

def building_detail(request, building_id):
    building = get_object_or_404(BuildingDetails, pk=building_id)
    forecast = get_live_forecast(building.name)
    latitude = forecast['venue_info']['venue_address_lat']
    longitude = forecast['venue_info']['venue_address_lng']
    return render(request, 'building_detail.html', {'building': building, 'forecast': forecast, 'latitude': latitude, 'longitude': longitude})