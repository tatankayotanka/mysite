from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.template import RequestContext
from .forms import TaskForm #UserForm
from .models import Task
from django.contrib import messages
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
'''def update_location(request, pk=None):
    obj = get_object_or_404(Location, pk=pk)
    form = LocationForm(request.POST or None,
                        request.FILES or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
           form.save()
           return redirect('/accounts/loggedin/locations/all/')
    return render(request, 'locations/location_update.html', {'form': form})'''
def update_task (request, task_id=None):
    task = get_object_or_404(Task, id=task_id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        task = form.save(commit=False)
        task.save()
        messages.success(request, "You just updated Task"+task.title)
        context={
            'task':task
        }
        messages.success(request, "You just updated Task"+task.title)

        return render(request, 'task/updateMessage.html', context)
    context = {
            'title':task.title,
            'task' : task,
            'form' : form,
        }
    return render(request,'task/task_update_form.html', context)
    #return render(request, 'task/detail.html', context)

def delete_task(request, task_id):
    #delete a certain task
    task = get_object_or_404(Task, pk=task_id)
    context = {
        'task': task,
    }
    task.delete()
    return render(request,'task/delete.html',context)
def create_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.assignee= request.POST.get('assignee')
        task.title = request.POST.get('title')
        task.progress = request.POST.get('progress')
        task.deadline = request.POST.get('deadline')
        task.description = request.POST.get('description')
        context = {
                    'task': task,
                    'form': form,
                    'error_message': 'input incorrect',
                }
        task.save()
        messages.success(request, 'Profile details updated.')
        #return render(request, 'task/detail.html', {'task': task})
        return render(request, 'task/create_detail.html', {'task': task})

    context = {
            "form": form,
        }
    return render(request, 'task/create_task.html', context)


def about(request):
    return render(request, 'task/about.html')

