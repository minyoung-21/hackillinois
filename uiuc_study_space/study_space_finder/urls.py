from django.urls import path

from . import views

urlpatterns = [
    path("", views.list_view, name="list_view"),
    path("details/", views.details_view, name="details_view"),
]