from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from .models import Task
#views are functions that usually return a HTTP response
#main page with task overview
def index(request):
    all_tasks = Task.objects.all()
    #template = loader.get_template('task/index.html')
    context = {
        'all_tasks':all_tasks,
    }
    return render(request, 'task/index.html',context)
#for review and edit task
def detail(request, task_id):
    #use get to retrieve an instance, not filter
    task = Task.objects.get(pk=task_id)
    context = {
        'task':task,
    }
    return render(request,'task/detail.html',context)
def delete_task(request, task_id):
    #delete a certain task
    task = Task.objects.get(pk=task_id)
    context = {
        'task': task,
    }
    task.delete()
    return render(request,'task/delete.html',context)
def create_task(request):
    task = Task()
    task.title

