from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNT_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
    name = models.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900),MaxValueValidator(2024)])
    active = models.fields.BooleanField(default=True)
    official_website = models.fields.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Listing(models.Model):
    class ListingType(models.TextChoices):
        ALBUM = 'AL'
        SINGLE = 'SI'
        EP = 'EP'
        COMPILATION = 'CO'
    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(validators=[MinValueValidator(1900),MaxValueValidator(2024)])
    type = models.fields.CharField(choices=ListingType.choices, max_length=5)
    def __str__(self):
        return self.name
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    