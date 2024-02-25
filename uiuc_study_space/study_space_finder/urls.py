from django.urls import path

from . import views

from django.urls import path
from .views import SampleFormView
# from django.contrib import admin
# from . import views
from django.urls import re_path as url

urlpatterns = [
    path("", views.list_view, name="list_view"),
    path('room/<int:room_id>/', views.room_details, name='room_details'),
    url(r'^$', SampleFormView.as_view()),

]
