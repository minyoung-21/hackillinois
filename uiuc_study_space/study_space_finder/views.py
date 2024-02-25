from django.shortcuts import render, get_object_or_404
from .models import RoomDetails

def list_view(request):
    return render(request, "list.html", {"room": RoomDetails.objects.all()})

def room_details(request, room_id):
    room = get_object_or_404(RoomDetails, pk=room_id)
    return render(request, "room_details.html", {"room": room})
