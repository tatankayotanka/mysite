from django.conf.urls import url
from . import views

app_name = 'task'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<task_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create_task/$', views.create_task, name='create_task'),
    url(r'^(?P<task_id>[0-9]+)/delete/$', views.delete_task, name='delete'),
    url(r'^(?P<task_id>[0-9]+)/update/$', views.update_task, name='update'),
    url(r'^about/$', views.about, name='about'),
]