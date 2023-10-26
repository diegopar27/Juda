from django.contrib import admin
from voter.models import Voter


@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    list_display = ('create_at', 'updated_at','name', 'type_of_document', 'document_number')
    list_filter = ('document_number',)

