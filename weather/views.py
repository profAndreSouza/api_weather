from django.views import View
from django.shortcuts import render

class WeatherView(View):
   
    def get(self, request):
        return render(request, "home.html")