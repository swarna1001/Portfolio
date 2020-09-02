from django.shortcuts import render, HttpResponse
from home import models
from home.models import Contact


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def project(request):
    return render(request, 'project.html')


def writings(request):
    return render(request, 'writings.html')
