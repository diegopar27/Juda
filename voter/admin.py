from django.contrib import admin
from voter.models import Voter


@admin.register(Voter)
class PreorderAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_of_document', 'document_number')
    list_filter = ('document_number',)

