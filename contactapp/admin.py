from django.contrib import admin
from .models import Team, Contact, Booking

# Register your models here.
admin.site.register(Team)
admin.site.register(Contact)
admin.site.register(Booking)