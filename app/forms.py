from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Type, Animal


class AnimalModelForm(ModelForm):

    class Meta:
        model = Animal
        fields = ['name', 'latinn', 'typee', 'info', 'image']
        labels = {'name': 'Animal name', 'info': 'Basic informations'}