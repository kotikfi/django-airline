# Generated by Django 3.2.3 on 2021-06-01 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('aircraft_id', models.IntegerField(primary_key=True, serialize=False)),
                ('manufacturer', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=20)),
                ('max_passengers', models.IntegerField()),
                ('max_speed', models.IntegerField()),
                ('range', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('icao', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('street', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('flight_hours', models.IntegerField(null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('passenger_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_id', models.IntegerField(primary_key=True, serialize=False)),
                ('dptTime', models.DateTimeField()),
                ('dstTime', models.DateTimeField()),
                ('aircraft_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Airlineapp.aircraft')),
                ('dispatcher_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='dispatcher', to='Airlineapp.employee')),
                ('dpt_airport_icao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='dpt_airport', to='Airlineapp.airport')),
                ('dst_airport_icao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='dst_airport', to='Airlineapp.airport')),
                ('flight_attendants', models.ManyToManyField(related_name='flight_attendants', to='Airlineapp.Employee')),
                ('passengers', models.ManyToManyField(to='Airlineapp.Passenger')),
                ('pilots', models.ManyToManyField(related_name='pilots', to='Airlineapp.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Check_in',
            fields=[
                ('check_in_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50, null=True)),
                ('airport_icao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Airlineapp.airport')),
                ('passengers', models.ManyToManyField(to='Airlineapp.Passenger')),
            ],
        ),
    ]
