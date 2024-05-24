from typing import Any
from bible_verse import main
from datetime import datetime
from random import randrange
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views import View
from django.shortcuts import render, redirect

from user.authentication import *

from .models import WeatherEntity
from .repositories import WeatherRepository
from .serializers import WeatherSerializer
from .forms import WeatherForm
from .exceptions import WeatherException

class WeatherView(View):

    authenticate = False
    user = None

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        token = request.COOKIES.get('jwt')

        error_code, _ = verifyToken(token)
        if error_code == 0:
            self.user = getAuthenticatedUser(token)
            self.authenticate = True
        
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        verse = main.get_bible_verse_en()
        repository = WeatherRepository(collectionName='weathers')
        try:
            weathers = list(repository.getAll())
            serializer = WeatherSerializer(data=weathers, many=True)
            if (serializer.is_valid()):
                modelWeather = serializer.save()
                objectReturn = {"weathers":modelWeather, "verse":verse}
            else:
                objectReturn = {"error":serializer.errors, "verse":verse}
        except WeatherException as e:
            objectReturn = {"error":e.message, "verse":verse}

        if not self.authenticate:
            objectReturn["errorAuth"] = "Usuário não autenticado"

        response = render(request, "home.html", objectReturn)

        if self.authenticate:
            newToken = refreshToken(self.user)
            response.set_cookie('jwt', newToken)
        
        return response
    

class WeatherGenerate(View):

    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weather = WeatherEntity(
            temperature=randrange(start=17, stop=40),
            date=datetime.now(),
            city='Sorocaba'
        )
        serializer = WeatherSerializer(data=weather.__dict__)
        if (serializer.is_valid()):
            repository.insert(serializer.data)
        else:
            print(serializer.errors)

        return redirect('Weather View')
    
class WeatherReset(View):

    def get(self, request): 
        repository = WeatherRepository(collectionName='weathers')
        repository.deleteAll()

        return redirect('Weather View')
    
class WeatherInsert(View):

    def get(self, request):
        weatherForm = WeatherForm()

        return render(request, "form.html", {"form":weatherForm})
    
    def post(self, request):
        weatherForm = WeatherForm(request.POST)
        if weatherForm.is_valid():
            serializer = WeatherSerializer(data=weatherForm.data)
            if (serializer.is_valid()):
                repository = WeatherRepository(collectionName='weathers')
                repository.insert(serializer.data)
            else:
                print(serializer.errors)
        else:
            print(weatherForm.errors)

        return redirect('Weather View')
    

class WeatherEdit(View):

    def get(self, request, id):
        repository = WeatherRepository(collectionName='weathers')
        weather = repository.getByID(id)
        weatherForm = WeatherForm(initial=weather)

        return render(request, "form_edit.html", {"form":weatherForm, "id":id})
    
    def post(self, request, id):
        weatherForm = WeatherForm(request.POST)
        if weatherForm.is_valid():
            serializer = WeatherSerializer(data=weatherForm.data)
            serializer.id = id
            if (serializer.is_valid()):
                repository = WeatherRepository(collectionName='weathers')
                repository.update(serializer.data, id)
            else:
                print(serializer.errors)
        else:
            print(weatherForm.errors)

        return redirect('Weather View')




class WeatherDelete(View):
    
    def get(self, request, id):
        repository = WeatherRepository(collectionName='weathers')
        repository.deleteByID(id)

        return redirect('Weather View')
    

class WeatherFilter(View):
    def post(self, request):
        data = request.POST.dict()
        data.pop('csrfmiddlewaretoken')

        verse = main.get_bible_verse_en()
        repository = WeatherRepository(collectionName='weathers')
        try:
            weathers = list(repository.get(data))
            serializer = WeatherSerializer(data=weathers, many=True)
            if (serializer.is_valid()):
                modelWeather = serializer.save()
                objectReturn = {"weathers":modelWeather, "verse":verse}
            else:
                objectReturn = {"error":serializer.errors, "verse":verse}
        except WeatherException as e:
            objectReturn = {"error":e.message, "verse":verse}
  
        return render(request, "home.html", objectReturn)