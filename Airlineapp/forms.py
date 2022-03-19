from django import forms
from .models import *


class DateInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        exclude = ['flight_id', 'passengers', 'flight_attendants', 'pilots']

        labels = {
            "dpt_airport": "Departure airport",
            "dst_airport": "Destination airport",
            "dpt_time": "Departure time",
            "dst_time": "Destination time",
        }

        widgets = {
            'aircraft': forms.Select(attrs={'class': 'form-control'}),
            'dispatcher': forms.Select(attrs={'class': 'form-control'}),
            'dpt_airport': forms.Select(attrs={'class': 'form-control'}),
            'dst_airport': forms.Select(attrs={'class': 'form-control'}),
            'dpt_time': DateInput(format='%Y-%m-%dT%H:%M', attrs={'class': 'form-control'}),
            'dst_time': DateInput(format='%Y-%m-%dT%H:%M', attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(FlightForm, self).__init__(*args, **kwargs)
        self.fields['dispatcher'].queryset = Employee.objects.filter(role__exact='dispatcher')


class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        exclude = ['passenger_id']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }

