from django.conf.urls import url
from . import views

urlpatterns = [
    #user gets to task, and uses the function index in views.py
    #/task/
    url(r'^$', views.index, name='index'),
    #/task/12/
    url(r'^(?P<task_id>[0-9]+)/$', views.detail, name='detail'),
]