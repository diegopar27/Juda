from django.contrib import admin
from neighborhood.models import Neighborhood


@admin.register(Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ('name_of_the_neighborhood','n_commune',)
    list_filter = ('name_of_the_neighborhood',)

