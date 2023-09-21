from django.contrib import admin
from leader.models import Leader


@admin.register(Leader)
class PreorderAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_of_document', 'document_number')
    list_filter = ('document_number',)

