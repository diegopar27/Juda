from django.contrib import admin
from commune.models import Commune


@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
    list_display = ('name_commune',)
