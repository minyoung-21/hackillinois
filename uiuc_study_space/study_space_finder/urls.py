from django.urls import path

from . import views

urlpatterns = [
    path("", views.list_view, name="list_view"),
    path('room/<int:room_id>/', views.room_details, name='room_details'),

]