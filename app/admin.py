from django.contrib import admin
from .models import PlantSpecies, PlantProfile


# Register your models here.

admin.site.register(PlantSpecies)
admin.site.register(PlantProfile)