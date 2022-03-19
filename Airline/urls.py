"""Airline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Airlineapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('flights/', views.flights, name='flights'),
    path('flights/new/', views.new_flight, name='new_flight'),
    path('flights/<int:pk>/edit/', views.edit_flight, name='edit_flight'),
    path('flights/<int:pk>/delete/', views.delete_flight, name='delete_flight'),
    path('flights/<int:pk>/detail/', views.flight_detail, name='flight_detail'),
    path('flights/<int:pk>/passengers/', views.flight_passengers, name='flight_passengers'),
    path('passengers/<int:pk>/', views.passenger_profile, name='passenger_profile'),
    path('passengers/<int:pk>/edit', views.edit_passenger_profile, name='edit_passenger_profile'),
    path('passengers/<int:pk>/delete/', views.delete_passenger, name='delete_passenger'),
    path('passengers/', views.passengers, name='passengers'),
    path('passengers/new/', views.new_passenger, name='new_passenger'),
]
