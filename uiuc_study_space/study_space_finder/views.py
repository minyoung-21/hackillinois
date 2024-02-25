from django.shortcuts import render, get_object_or_404
from .models import RoomDetails
# from .models import BuildingDetails
# from .utils import get_live_forecast
# from models import Building
# building_names = [building.name for building in Building.query.all()]
# set_building_names = set(building_names)
# building_data = get_live_forecast(set_building_names)

def list_view(request):
    room = RoomDetails.objects.all()

    if request.GET.get('outlet_availability'):
        room = room.filter(outlet_availability=True)
    if request.GET.get('tables_availability'):
        room = room.filter(tables_availability=True)
    if request.GET.get('open_space_availability'):
        room = room.filter(open_space_availability=True)

    return render(request, "list.html", {"room": room})


# def building_detail(request, building_id):
#     building = get_object_or_404(BuildingDetails, pk=building_id)
#     forecast = get_live_forecast(building.name)
#     latitude = forecast['venue_info']['venue_address_lat']
#     longitude = forecast['venue_info']['venue_address_lng']
#     return render(request, 'building_detail.html', {'building': building, 'forecast': forecast, 'latitude': latitude, 'longitude': longitude})

def room_details(request, room_id):
    room = get_object_or_404(RoomDetails, pk=room_id)
    return render(request, "room_details.html", {"room": room})




from django.http import HttpResponse

import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
 


 
from django.shortcuts import render
 
# relative import of forms
from django.views.generic import CreateView

 
from .models import MyModel, MyModelForm


class MyCreateView(CreateView):
    form_class = MyModelForm
    model = MyModel

from django.views.generic import FormView

from .forms import SampleForm


class SampleFormView(FormView):
    form_class = SampleForm
    template_name = "map_template.html"
def maps(request):
    c = "map heck yeh"
    return render(request, 'map_template.html', {'maps': c})

