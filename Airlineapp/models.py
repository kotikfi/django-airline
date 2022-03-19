from django.db import models


class Aircraft(models.Model):
    aircraft_id = models.IntegerField(primary_key=True)
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=20)
    max_passengers = models.IntegerField()
    max_speed = models.IntegerField()
    range = models.IntegerField()

    def __str__(self):
        return f'{self.manufacturer} {self.model}'


class Airport(models.Model):
    icao = models.CharField(primary_key=True, max_length=4)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f'[{self.icao}] {self.name}'


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    flight_hours = models.IntegerField(null=True)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'[{self.employee_id}] {self.first_name} {self.last_name}'


class Passenger(models.Model):
    passenger_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Check_in(models.Model):
    check_in_id = models.IntegerField(primary_key=True)
    airport = models.ForeignKey(Airport, on_delete=models.DO_NOTHING)
    passengers = models.ManyToManyField(Passenger)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50, null=True)


class Flight(models.Model):
    flight_id = models.IntegerField(primary_key=True)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.DO_NOTHING)
    dispatcher = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, related_name='dispatcher')
    dpt_airport = models.ForeignKey(Airport, on_delete=models.DO_NOTHING, related_name='dpt_airport')
    dst_airport = models.ForeignKey(Airport, on_delete=models.DO_NOTHING, related_name='dst_airport')
    pilots = models.ManyToManyField(Employee, related_name='pilots')
    flight_attendants = models.ManyToManyField(Employee, related_name='flight_attendants')
    passengers = models.ManyToManyField(Passenger)
    dpt_time = models.DateTimeField()
    dst_time = models.DateTimeField()

    def __str__(self):
        return f'Flight no. {self.flight_id} From: {self.dpt_airport} -> {self.dst_airport}'