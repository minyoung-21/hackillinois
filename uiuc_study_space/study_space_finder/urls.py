from django.urls import path

from . import views

urlpatterns = [
    path("", views.list_view, name="list_view"),
    path('building/<int:building_id>/', views.building_detail, name='building_detail'),

]