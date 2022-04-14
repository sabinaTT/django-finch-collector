from django.shortcuts import render
from django.views import View # View class to handle requests
from django.http import HttpResponse # a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


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

class Finch_List(TemplateView):
    template_name = "finch_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context['finches'] = Finch.objects.filter(name__icontains=name)
            context['header'] = f'Searching for {name}'
        else:
            context['finches'] = Finch.objects.all()
            context['header'] = 'Finches'

        return context

class Finch_Create(CreateView):
    model = Finch
    fields = '__all__'
    # template_name = 'finch_create.html'
    success_url = '/finches/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/finches')

class Finch_Detail(DetailView):
    model = Finch
    template_name = 'finch_detail.html'

class Finch_Update(UpdateView):
    model = Finch
    fields = ['name', 'img', 'age', 'family']
    template_name = 'finch_update.html'
    # success_url = '/finches'
    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.pk})

class Finch_Delete(DeleteView):
    model = Finch
    template_name = 'finch_delete_confirmation.html'
    success_url = '/finches/'

def profile(request, username):
    user = User.objects.get(username=username)
    finches = Finch.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'finches': finches })