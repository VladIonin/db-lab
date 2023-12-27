from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'aircraft', AircraftViewSet)
router.register(r'airport', AirportsViewSet)

router.register(r'seat', SeatsViewSet)
router.register(r'animal', AnimalsViewSet)
router.register(r'booking', BookingViewSet)
router.register(r'baggage', BaggageViewSet)
router.register(r'ticket', TicketsViewSet)
router.register(r'flight', FlightsViewSet)
router.register(r'passenger', PassengersViewSet)

router.register(r'odometer', OdometerReadingViewSet)
router.register(r'engine', EnginesViewSet)
router.register(r'pilot', PilotsViewSet)
router.register(r'personal', PersonalViewSet)
router.register(r'maintenance', MaintenanceReadingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('drf-auth/', include('rest_framework.urls'))
    # path('aircraft-by-capacity/<int:capacity>', aircraft_by_capacity),
    # path('total-dist/<int:aircraft_id>', total_distance),
    # path('pilots-by-airport/<int:airport_id>', pilots_by_airport),
    # path('passengers_by_flight/<str:flight_number>', passengers_by_flight),
]
