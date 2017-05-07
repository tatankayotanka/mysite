from django.http import HttpResponse
from django.template import loader
from .models import Task
#views are functions that usually return a HTTP response
def index(request):
    all_tasks = Task.objects.all()
    template = loader.get_template('task/index.html')
    context = {
        'all_tasks':all_tasks,
    }
    return HttpResponse(template.render(context, request))

def detail(request, task_id):
    return HttpResponse("<h2>Details for Album " +str(task_id) +"</h2>")