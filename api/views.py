from django.db.models import Sum
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import \
    AircraftSerializer, AirportsSerializer, AnimalsSerializer, BookingSerializer, EnginesSerializer, \
    FlightsSerializer, PassengersSerializer, TicketsSerializer, PilotsSerializer, PersonalSerializer, \
    BaggageSerializer, SeatsSerializer, OdometerReadingSerializer, MaintenanceSerializer

from .models import Flights, Pilots, Personal, Passengers, Aircraft, Airports, Animals, Booking, Engines, Tickets, \
    Baggage, Seats, OdometerReading, Maintenance


class IsStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
    permission_classes = [IsStaffOrReadOnly]


class AirportsViewSet(viewsets.ModelViewSet):
    queryset = Airports.objects.all()
    serializer_class = AirportsSerializer
    permission_classes = [IsStaffOrReadOnly]


class AnimalsViewSet(viewsets.ModelViewSet):
    queryset = Animals.objects.all()
    serializer_class = AnimalsSerializer
    permission_classes = [IsStaffOrReadOnly]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsStaffOrReadOnly]


class EnginesViewSet(viewsets.ModelViewSet):
    queryset = Engines.objects.all()
    serializer_class = EnginesSerializer
    permission_classes = [IsStaffOrReadOnly]


class FlightsViewSet(viewsets.ModelViewSet):
    queryset = Flights.objects.all()
    serializer_class = FlightsSerializer
    permission_classes = [IsStaffOrReadOnly]


class PassengersViewSet(viewsets.ModelViewSet):
    queryset = Passengers.objects.all()
    serializer_class = PassengersSerializer
    permission_classes = [IsStaffOrReadOnly]


class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer
    permission_classes = [IsStaffOrReadOnly]


class PilotsViewSet(viewsets.ModelViewSet):
    queryset = Pilots.objects.all()
    serializer_class = PilotsSerializer
    permission_classes = [IsStaffOrReadOnly]


class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
    permission_classes = [IsStaffOrReadOnly]


class BaggageViewSet(viewsets.ModelViewSet):
    queryset = Baggage.objects.all()
    serializer_class = BaggageSerializer
    permission_classes = [IsStaffOrReadOnly]


class SeatsViewSet(viewsets.ModelViewSet):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer
    permission_classes = [IsStaffOrReadOnly]


class OdometerReadingViewSet(viewsets.ModelViewSet):
    queryset = OdometerReading.objects.all()
    serializer_class = OdometerReadingSerializer
    permission_classes = [IsStaffOrReadOnly]


class MaintenanceReadingViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
    permission_classes = [IsStaffOrReadOnly]

# @api_view(['GET'])
# def aircraft_by_capacity(request, capacity):
#     aircraft_types = Aircraft.objects.filter(passenger_capacity__gte=capacity)
#     serializer = AircraftSerializer(aircraft_types, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def total_distance(request, aircraft_id):
#     try:
#         flight = Flights.objects.filter(aircraft_id=aircraft_id)
#         total_dist = flight.aggregate(Sum('distance_traveled'))['distance_traveled__sum']
#         if total_dist is not None:
#             response_data = {'total_dist': total_dist}
#             return Response(response_data, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'No flights found for the specified aircraft ID.'},
#                             status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @api_view(['GET'])
# def pilots_by_airport(request, airport_id):
#     try:
#         pilots = Pilots.objects.filter(airport_of_work=airport_id)
#         if not pilots.exists():
#             raise Pilots.DoesNotExist
#         serializer = PilotsSerializer(pilots, many=True)
#         return Response(serializer.data)
#     except Pilots.DoesNotExist:
#         return Response({'error': 'Pilots or Airport not found'}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @api_view(['GET'])
# def passengers_by_flight(request, flight_number):
#     try:
#         passengers = Passengers.objects.filter(booking__ticket__flight__flight_number=flight_number)
#         serializer = PassengersSerializer(passengers, many=True)
#         return Response(serializer.data)
#     except Passengers.DoesNotExist:
#         return Response({"message": "Passengers not found for the flight number"}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
