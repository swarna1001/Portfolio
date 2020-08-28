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


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']

        save_contact = Contact(name=name, email=email, desc=desc)
        save_contact.save()
        print("the data has been entered in the db!")




    return render(request, 'contact.html')
