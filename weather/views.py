from bible_verse import main
from datetime import datetime
from random import randrange
from django.views import View
from django.shortcuts import render, redirect
from .models import WeatherEntity
from .repositories import WeatherRepository

class WeatherView(View):
    def get(self, request):
        verse = main.get_bible_verse()
        repository = WeatherRepository(collectionName='weathers')
        weathers = repository.getAll()
        return render(request, "home.html", {"weathers":weathers, "verse":verse})
    

class WeatherGenerate(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        # wheater = WeatherEntity(
        #     temperature=randrange(start=17, stop=40),
        #     date=datetime.now()
        # )
        wheater = {
            "temperature" : 28,
            "date": "hoje"
            }
        repository.insert(wheater)

        return redirect('Weather View')