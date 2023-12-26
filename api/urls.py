from django.urls import path, include
from .views import aircraft_by_capacity, total_distance, pilots_by_airport, fire_them, passengers_by_flight, flights

urlpatterns = [
    path('flights/', flights, name='flights'),                                                   # Only admin

    path('auth/', include('rest_framework.urls')),                                               # Anybody
    path('capacity/<int:capacity>', aircraft_by_capacity, name='aircraft_by_capacity'),          # Anybody
    path('dist/<int:aircraft_id>', total_distance, name='total_distance'),                       # Anybody

    path('pilots/<int:airport_id>', pilots_by_airport, name='pilots_by_airport'),                # Authenticated users
    path('fire_them/', fire_them, name='fire_them'),  # Authenticated users
    path('passengers/<str:flight_number>/', passengers_by_flight, name='passengers_by_flight'),  # Authenticated users

]
