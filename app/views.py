from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.models import *
from django.urls import reverse_lazy, reverse
from app.forms import AnimalModelForm


def index(request): 

    num_animals = Animal.objects.all().count()  
    animals = Animal.objects.order_by('-typee')
 
    context = { 
        'num_animals': num_animals, 
        'animals': animals 
    } 
 
    return render(request, 'index.html', context=context) 


class AnimalDetailView(DetailView):
    model = Animal

    context_object_name = 'animal_detail'  
    template_name = 'detail.html' 

 
class AnimalListView(ListView):
    model = Animal
    template_name = 'index.html'


class AddAnimal(CreateView):
    model = Animal
    fields = ['name', 'latinn', 'typee', 'info', 'image']


class UpdateAnimal(UpdateView):
    model = Animal
    template_name = 'update.html'
    form_class = AnimalModelForm


class DeleteAnimal(DeleteView):
    model = Animal
    success_url = reverse_lazy('animals')


# WIP 
class TypeListView(ListView):
    model = Animal
    template_name = 'type_list.html'
    context_object_name = 'type'
    queryset = Animal.objects.order_by('name').all()


class GalleryView(ListView):
    model = Animal
    template_name = 'gallery.html'
    context_object_name = 'gallery'


