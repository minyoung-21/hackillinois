from django.shortcuts import render, get_object_or_404
from .models import RoomDetails

def list_view(request):
    return render(request, "list.html", {"room": RoomDetails.objects.all()})

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
