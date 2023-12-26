from django.db import models


class Aircraft(models.Model):
    aircraft_id = models.AutoField(primary_key=True, blank=True)
    type = models.ForeignKey('AircraftTypes', models.DO_NOTHING, db_column='type', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Aircraft'


class AircraftTypes(models.Model):
    name = models.TextField(unique=True, blank=True, null=True)
    passenger_capacity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Aircraft_Types'


class Airports(models.Model):
    airport_id = models.AutoField(primary_key=True, blank=True)
    airport_code = models.TextField(blank=True, null=True)
    city = models.ForeignKey('Cities', models.DO_NOTHING, db_column='city', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Airports'


class Animals(models.Model):
    baggage = models.ForeignKey('Baggage', models.DO_NOTHING, db_column='baggage', blank=True, null=True)
    animal_id = models.AutoField(primary_key=True, blank=True)
    animal_weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Animals'


class Baggage(models.Model):
    baggage_id = models.AutoField(primary_key=True, blank=True)
    booking = models.ForeignKey('Booking', models.DO_NOTHING, db_column='booking', blank=True, null=True)
    weight_in_kilogram = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Baggage'


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True, blank=True)
    ticket = models.ForeignKey('Tickets', models.DO_NOTHING, db_column='ticket', blank=True, null=True)
    passenger = models.ForeignKey('Passengers', models.DO_NOTHING, db_column='passenger', blank=True, null=True)
    booking_status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Booking'


class Cities(models.Model):
    city_id = models.AutoField(primary_key=True, blank=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cities'


class Engines(models.Model):
    engine_id = models.AutoField(primary_key=True, blank=True)
    max_mileage = models.IntegerField(blank=True, null=True)
    current_mileage = models.IntegerField(blank=True, null=True)
    plane_owner = models.ForeignKey(Aircraft, models.DO_NOTHING, db_column='plane_owner', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Engines'


class EventTypes(models.Model):
    type_id = models.AutoField(primary_key=True, blank=True)
    type_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Event_Types'


class Events(models.Model):
    event_id = models.AutoField(primary_key=True, blank=True)
    event_type = models.ForeignKey(EventTypes, models.DO_NOTHING, db_column='event', to_field=None, blank=True, null=True)
    scene_of_accident = models.ForeignKey(Aircraft, models.DO_NOTHING, db_column='scene_of_accident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Events'


class FlightStatus(models.Model):
    flight = models.ForeignKey('Flights', models.DO_NOTHING, db_column='flight', blank=True)
    canceled = models.BooleanField(blank=True, null=True)
    technical = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Flight_Status'


class Flights(models.Model):
    flight_id = models.AutoField(primary_key=True, blank=True)
    flight_number = models.TextField(unique=True, blank=True, null=True)
    aircraft = models.ForeignKey(Aircraft, models.DO_NOTHING, blank=True, null=True)
    pilot = models.ForeignKey('Pilots', models.DO_NOTHING, db_column='pilot', blank=True)
    flight_delay_in_hours = models.IntegerField(blank=True, null=True)
    time_of_arrival = models.TextField(blank=True, null=True)  # This field type is a guess.
    time_of_departure = models.TextField(blank=True, null=True)  # This field type is a guess.
    airport_of_arrive = models.ForeignKey(Airports, models.DO_NOTHING, db_column='airport_of_arrive', blank=True, null=True)
    airport_of_departure = models.ForeignKey(Airports, models.DO_NOTHING, db_column='airport_of_departure', related_name='flights_airport_of_departure_set', blank=True, null=True)
    distance_traveled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Flights'


class JobTitle(models.Model):
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Job_Title'


class Maintenance(models.Model):
    maintenance_id = models.AutoField(primary_key=True, blank=True)
    date_of_maintenance = models.DateField(blank=True, null=True)
    inspector = models.ForeignKey('Personal', models.DO_NOTHING, db_column='inspector', blank=True, null=True)
    plane = models.ForeignKey(Aircraft, models.DO_NOTHING, db_column='plane', blank=True, null=True)
    result = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Maintenance'


class OdometerReading(models.Model):
    odometer_id = models.AutoField(primary_key=True, blank=True)
    aircraft = models.ForeignKey(Aircraft, models.DO_NOTHING, db_column='aircraft', blank=True, null=True)
    flight = models.ForeignKey(Flights, models.DO_NOTHING, db_column='flight', blank=True, null=True)
    odometer_reading = models.IntegerField(blank=True, null=True)
    reading_time = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Odometer_Reading'


class Passengers(models.Model):
    passenger_id = models.AutoField(primary_key=True, blank=True)
    passport = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Passengers'


class Personal(models.Model):
    personal_id = models.AutoField(primary_key=True, blank=True)
    name = models.TextField(blank=True, null=True)
    job_title = models.ForeignKey(JobTitle, models.DO_NOTHING, db_column='job_title', blank=True, null=True)
    working_place = models.ForeignKey(Airports, models.DO_NOTHING, db_column='working_place', blank=True, null=True)
    family = models.TextField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    start_of_work = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Personal'


class Pilots(models.Model):
    pilot_id = models.AutoField(primary_key=True, blank=True)
    name_of_pilot = models.TextField(blank=True, null=True)
    start_of_working = models.DateField(blank=True, null=True)
    hours_passed = models.IntegerField(blank=True, null=True)
    airport_of_work = models.ForeignKey(Airports, models.DO_NOTHING, db_column='airport_of_work', blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Pilots'


class Seats(models.Model):
    place_id = models.AutoField(primary_key=True, blank=True)
    plane = models.ForeignKey(Aircraft, models.DO_NOTHING, db_column='plane', blank=True, null=True)
    place_number = models.IntegerField(blank=True, null=True)
    place_class = models.TextField(blank=True, null=True)
    place_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Seats'


class Tickets(models.Model):
    ticket_id = models.AutoField(primary_key=True, blank=True)
    flight = models.ForeignKey(Flights, models.DO_NOTHING, db_column='flight', blank=True, null=True)
    siting_place = models.ForeignKey(Seats, models.DO_NOTHING, db_column='siting_place', blank=True, null=True)
    ticket_date = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Tickets'
