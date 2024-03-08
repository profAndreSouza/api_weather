from django.db import models

class WeatherEntity:

    def __init__(self, temperature, date,
                 city='', atmosphericPressure='',
                 humidity='', weather='') -> None:
        self.temperature = temperature
        self.city = city
        self.atmosphericPressure = atmosphericPressure
        self.humidity = humidity
        self.weather = weather
        self.date = date

    def __str__(self) -> str:
        return (f"Weather <{self.temperature}>")
