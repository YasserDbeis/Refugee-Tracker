from django.contrib import admin

# Register your models here.
from .models import Location, Population

admin.site.register(Location)
admin.site.reigster(Population)