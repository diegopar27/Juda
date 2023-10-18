from django.contrib import admin
from neighborhood.models import Neighborhood,Neighborhood_leader


@admin.register(Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ('name_of_the_neighborhood',)
    list_filter = ('name_of_the_neighborhood',)

@admin.register(Neighborhood_leader)
class Neighborhood_leaderAdmin(admin.ModelAdmin):
    list_display = ('neighborhoods','leaders',)