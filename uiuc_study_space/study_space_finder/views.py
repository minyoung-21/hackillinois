from django.shortcuts import render
from .models import BuildingDetails

def list_view(request):
    return render(request, "list.html", {"buildings": BuildingDetails.objects.all()})