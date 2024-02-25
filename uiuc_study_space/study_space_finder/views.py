from django.shortcuts import render, get_object_or_404
from .models import BuildingDetails

def list_view(request):
    return render(request, "list.html", {"buildings": BuildingDetails.objects.all()})

def building_detail(request, building_id):
    building = get_object_or_404(BuildingDetails, pk=building_id)
    return render(request, "building_detail.html", {"building": building})