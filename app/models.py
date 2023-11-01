from django.db import models

# Create your models here.


# Choices for soil mix
SOIL_MIX_CHOICES = [
    ('sandy', 'Sandy'),
    ('loamy', 'Loamy'),
    ('clay', 'Clay'),
    ('peaty', 'Peaty'),
]

# Choices for soil conditions
SOIL_CONDITIONS_CHOICES = [
    ('well_drained', 'Well-Drained'),
    ('moist', 'Moist'),
    ('dry', 'Dry'),
]

# Choices for light conditions
LIGHT_CONDITIONS_CHOICES = [
    ('full_sun', 'Full Sun'),
    ('partial_sun', 'Partial Sun'),
    ('shade', 'Shade'),
]

# Choices for toxicity to animals
TOXICITY_CHOICES = [
    ('none', 'None'),
    ('dog', 'Dog'),
    ('cat', 'Cat'),
]


class PlantSpecies(models.Model):
    # Fields for plant species information
    name = models.CharField(max_length=255, unique=True, blank=True)
    common_name = models.CharField(max_length=255, unique=True, blank=True)
    watering_frequency = models.IntegerField()
    soil_mix = models.CharField(max_length=20, choices=SOIL_MIX_CHOICES)
    soil_conditions = models.CharField(max_length=20, choices=SOIL_CONDITIONS_CHOICES)
    light_conditions = models.CharField(max_length=20, choices=LIGHT_CONDITIONS_CHOICES)
    toxicity_to_animals = models.CharField(max_length=20, choices=TOXICITY_CHOICES, default='none')

    class Meta:
        verbose_name='Plant Species'
        verbose_name_plural='Plant Species'

    def __str__(self):
        return self.common_name


class PlantProfile(models.Model):
    # Fields for plant profile information
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    location = models.CharField(max_length=255)
    plant_origin = models.CharField(max_length=255)
    soil_mix = models.CharField(max_length=255)
    last_repot = models.DateField()
    moss_poles = models.BooleanField(default=False)
    progress_photos = models.ImageField(upload_to='plant_photos/', blank=True, null=True)
    misc_notes = models.TextField(blank=True)

    # Foreign key to link PlantProfile to PlantSpecies
    species = models.ForeignKey(PlantSpecies, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


