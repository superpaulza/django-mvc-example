from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse('Hello World!')

def hello_id(request, id):
    return HttpResponse('Hello World! id=' + str(id))

def hello_id_name(request, id, name):
    return HttpResponse('Hello World! id=' + str(id) + name)

def article(request, year, slag):
    return HttpResponse('Article Year=' + str(year) + 'from' + slag)

# def index(request):
#     return render(request, 'index.html')

def index(request):
    id = '001'
    name = 'Somchai'
    email = 'somchai@gmail.com'

    activities = [
        'Football',
        'Running',
        'Badminton'
    ]

    return render(request, 'index.html', {
        'id': id,
        'name': name,
        'email': email,
        'activities': activities
    })