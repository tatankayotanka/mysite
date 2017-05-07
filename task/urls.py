from django.conf.urls import url
from . import views

urlpatterns = [
    #user gets to task, and uses the function index in views.py
    url(r'^$', views.index, name='index'),
]