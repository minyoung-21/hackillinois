from django.urls import path
from .views import SampleFormView
# from django.contrib import admin
# from . import views
from django.urls import re_path as url
urlpatterns = [
# url(r'^admin/', admin.site.urls),
url(r'^$', SampleFormView.as_view()),
    # path("", views.maps, name="index"),
]