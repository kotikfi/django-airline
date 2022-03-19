from django.contrib import admin
from .models import *

admin.site.register(Aircraft)
admin.site.register(Airport)
admin.site.register(Employee)
admin.site.register(Passenger)
admin.site.register(Check_in)
admin.site.register(Flight)