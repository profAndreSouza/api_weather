from django.urls import path
from weather.views import *

urlpatterns = [
    path('', WeatherView.as_view(), name='Weather View'),
    path('insert', WeatherInsert.as_view(), name='Weather Insert'),
    path('edit/<id>/', WeatherEdit.as_view(), name='Weather Edit'),
    path('generate', WeatherGenerate.as_view(), name='Weather Generate'),
    path('reset', WeatherReset.as_view(), name='Weather Reset'),
]
