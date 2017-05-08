from django.conf.urls import url
from . import views

urlpatterns = [
   #url(r'^register/$', views.register, name='register'),
    #url(r'^login_user/$', views.login_user, name='login_user'),
   # url(r'^logout_user/$', views.logout_user, name='logout_user'),
    #user gets to task, and uses the function index in views.py
    #/task/
    url(r'^$', views.index, name='index'),
    #/task/12/ might need to consider to /task/12/edit
    url(r'^(?P<task_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create_task/$', views.create_task, name='create_task'),
    url(r'^(?P<task_id>[0-9]+)/delete/$', views.delete_task, name='delete'),
    url(r'^(?P<task_id>[0-9]+)/update/$', views.update_task, name='update'),

]