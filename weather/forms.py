from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from .models import WeatherEntity

class WeatherForm(forms.Form):
    temperature = forms.FloatField()
    date = forms.DateTimeField()
    city = forms.CharField(max_length=255)
    atmosphericPressure = forms.FloatField(required=False)
    humidity = forms.FloatField(required=False)
    weather = forms.CharField(max_length=255, required=False)

    # def __init__(self, *args, **kwargs):
    #     self.fields['temperature'].label = 'Temperatura'