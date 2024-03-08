from django.urls import path
from weather.views import WeatherView

urlpatterns = [
    path('', WeatherView.as_view()),

]
