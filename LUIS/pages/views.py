# importing the necessary libraries
from django.shortcuts import render
from pages.models import Registration


def index(request):
    return render(request, 'index.html')


def registered(request):
    first_name = request.POST['fn']
    last_name = request.POST['ln']

    person = Registration(first_name=first_name, last_name=last_name)
    person.save()
    return render(request, 'registered.html', {'fn': first_name})