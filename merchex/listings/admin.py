from re import L
from django.contrib import admin

from .models import Band, Listing

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'year_formed', 'active', 'official_website')
    
class ListingAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'sold', 'year', 'type','band')

admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
