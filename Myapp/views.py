from django.shortcuts import render

from django.http import HttpResponse
from Myapp.models import Student

# Create your views here.
def hello(request):
    return HttpResponse("Hi there Grace")

def evenodd(request):
    x = 25
    if x%2==0:
        return HttpResponse("Number is even")
    else:
        return HttpResponse("Number is odd")

def index(request):
    return render(request, 'index.html')

def table(request):
    return render(request, 'table.html')

def variables(request):
    details={
        "firstname":"Grace",
        "lastname":"eMobilis",
        "age":60,
        "place":"Westlands",
    }
    return render(request, 'variable.html',details)

def employees(request):
    details1={
        "first":"Grace Wambui",
        "sec": 5763,
        "third": 45000,
    }
    return render(request,'employees.html',details1)

def images(request):
    return render(request, 'images.html')

def background(request):
    return render(request, 'background.html')

def members(request):
    all=Student.objects.all().values()
    details={
        "members":all
    }
    return render(request, 'members.html', details)