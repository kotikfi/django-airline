from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    return render(request, 'Airlineapp/index.html')


def flights(request):
    flights = Flight.objects.all()
    aircrafts = Aircraft.objects.all()
    return render(request, 'Airlineapp/flights.html', {'flights': flights, 'aircrafts': aircrafts})


def new_flight(request):
    flight_form = FlightForm()
    if request.method == 'POST':
        flight_form = FlightForm(request.POST)
        if flight_form.is_valid():
            flight_form.save()
            return redirect(flights)

    return render(request, 'Airlineapp/new_flight.html', {'flight_form': flight_form})


def edit_flight(request, pk):
    flight = Flight.objects.get(flight_id=pk)
    flight_form = FlightForm(instance=flight)
    if request.method == 'POST':
        flight_form = FlightForm(request.POST, instance=flight)
        if flight_form.is_valid():
            flight_form.save()
            return redirect(flights)

    return render(request, 'Airlineapp/edit_flight.html', {'flight_form': flight_form})


def delete_flight(request, pk):
    flight = Flight.objects.get(flight_id=pk)
    if request.method == "POST":
        flight.delete()
        return redirect(flights)

    return render(request, 'Airlineapp/delete_flight.html', {'flight': flight})


def flight_detail(request, pk):
    flight = Flight.objects.get(flight_id=pk)

    return render(request, 'Airlineapp/flight_detail.html', {'flight': flight})


def flight_passengers(request, pk):
    flight = Flight.objects.get(flight_id=pk)
    passengers = flight.passengers.all()
    return render(request, 'Airlineapp/flight_passengers.html', {'flight': flight, 'passengers': passengers})


def passenger_profile(request, pk):
    passenger = Passenger.objects.get(passenger_id=pk)

    return render(request, 'Airlineapp/passenger_profile.html', {'passenger': passenger})


def edit_passenger_profile(request, pk):
    passenger = Passenger.objects.get(passenger_id=pk)
    passenger_form = PassengerForm(instance=passenger)
    if request.method == 'POST':
        passenger_form = PassengerForm(request.POST, instance=passenger)
        if passenger_form.is_valid():
            passenger_form.save()
            return redirect(passenger_profile, pk)
    return render(request, 'Airlineapp/edit_passenger_profile.html', {'passenger_form': passenger_form, 'passenger': passenger})


def delete_passenger(request, pk):
    passenger = Passenger.objects.get(passenger_id=pk)
    if request.method == "POST":
        passenger.delete()
        return redirect(passengers)

    return render(request, 'Airlineapp/delete_passenger.html', {'passenger': passenger})


def passengers(request):
    passengers = Passenger.objects.all()

    return render(request, 'Airlineapp/passengers.html', {'passengers': passengers})


def new_passenger(request):
    passenger_form = PassengerForm()
    if request.method == 'POST':
        passenger_form = PassengerForm(request.POST)
        if passenger_form.is_valid():
            passenger_form.save()
            return redirect(passengers)

    return render(request, 'Airlineapp/new_passenger.html', {'passenger_form': passenger_form})