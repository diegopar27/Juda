from django.contrib import admin
from candidate.models import Candidate


@admin.register(Candidate)
class PreorderAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_of_document', 'document_number')
    list_filter = ('document_number',)