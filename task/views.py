from django.http import HttpResponse
#views are functions that usually return a HTTP response
def index(request):
    return HttpResponse("<h1>Welcome to TaskCracker</h1>")