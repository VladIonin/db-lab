from django.db import models
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import AircraftTypesSerializer, PilotsSerializer, PersonalSerializer, PassengersSerializer, \
    FlightsSerializer
from .models import AircraftTypes, Flights, Pilots, Personal, Passengers


@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def flights(request):
    flight = Flights.objects.all()
    serializer = FlightsSerializer(flight, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def aircraft_by_capacity(request, capacity):
    aircraft_types = AircraftTypes.objects.filter(passenger_capacity__gte=capacity)
    serializer = AircraftTypesSerializer(aircraft_types, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def total_distance(request, aircraft_id):
    try:
        flight = Flights.objects.filter(aircraft_id=aircraft_id)
        total_dist = flight.aggregate(models.Sum('distance_traveled'))['distance_traveled__sum']
        if total_dist is not None:
            response_data = {'total_dist': total_dist}
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No flights found for the specified aircraft ID.'},
                            status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def pilots_by_airport(request, airport_id):
    try:
        pilots = Pilots.objects.filter(airport_of_work=airport_id)
        if not pilots.exists():
            raise Pilots.DoesNotExist
        serializer = PilotsSerializer(pilots, many=True)
        return Response(serializer.data)
    except Pilots.DoesNotExist:
        return Response({'error': 'Pilots or Airport not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def fire_them(request):
    try:
        maintenance = Personal.objects.filter(maintenance__result='Broken')
        serializer = PersonalSerializer(maintenance, many=True)
        return Response(serializer.data)
    except Personal.DoesNotExist:
        return Response({'error': 'Inspectors not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def passengers_by_flight(request, flight_number):
    try:
        passengers = Passengers.objects.filter(booking__ticket__flight__flight_number=flight_number)
        serializer = PassengersSerializer(passengers, many=True)
        return Response(serializer.data)
    except Passengers.DoesNotExist:
        return Response({"message": "Passengers not found for the flight number"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
