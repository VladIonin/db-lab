from rest_framework import serializers
from .models import AircraftTypes, Flights, Pilots, Personal, Passengers


class AircraftTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AircraftTypes
        fields = '__all__'


class FlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = '__all__'


class PilotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilots
        fields = '__all__'


class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = ['personal_id', 'name', 'salary', 'start_of_work']


class PassengersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passengers
        fields = '__all__'
