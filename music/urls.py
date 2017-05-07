from django.conf.urls import url
from . import views

urlpatterns = [
    #user gets to music, and uses the function index in views.py
    url(r'^$', views.index, name='index'),
]