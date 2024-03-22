from django.urls import path
from weather.views import WeatherView, WeatherGenerate, WeatherReset, WeatherInsert

urlpatterns = [
    path('', WeatherView.as_view(), name='Weather View'),
    path('insert', WeatherInsert.as_view(), name='Weather Insert'),
    path('generate', WeatherGenerate.as_view(), name='Weather Generate'),
    path('reset', WeatherReset.as_view(), name='Weather Reset'),
]
