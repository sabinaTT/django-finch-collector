from django.shortcuts import render
from django.views import View # View class to handle requests
from django.http import HttpResponse # a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Finch

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"
    # Here we are adding a method that will be run when we are dealing with a GET request
    # def get(self, request):
        # Here we are returning a generic response
        # This is similar to response.send() in express
        # return HttpResponse("Finch Home")

class About(TemplateView):
    template_name = "about.html"

class Index(TemplateView):
    template_name = "index.html"

class Finch:
    def __init__(self, name, age, family):
        self.name = name 
        self.age = age
        self.family = family

finches = [
    Finch('Julia', 12, 'Estrildidae'),
    Finch('Sergius', 3, 'Estrildidae'),
]

class Finch_List(TemplateView):
    template_name = "finch_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['finches'] = finches

        return context