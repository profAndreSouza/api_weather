from django.urls import path
from weather.views import WeatherView, WeatherGenerate

urlpatterns = [
    path('', WeatherView.as_view(), name='Weather View'),
    path('generate', WeatherGenerate.as_view(), name='Weather Generate'),
]
