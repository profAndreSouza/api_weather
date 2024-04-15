from rest_framework import serializers
from .models import WeatherEntity

class WeatherSerializer(serializers.Serializer):
    id = serializers.CharField(allow_blank=True, required=False)
    temperature = serializers.FloatField()
    date = serializers.DateTimeField()
    city = serializers.CharField(max_length=255, allow_blank=True)
    atmosphericPressure = serializers.FloatField(required=False)
    humidity = serializers.FloatField(required=False)
    weather = serializers.CharField(max_length=255, allow_blank=True)

    def create(self, validated_data):
        return WeatherEntity(**validated_data)