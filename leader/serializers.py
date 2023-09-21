from rest_framework.serializers import ModelSerializer
from leader.models import Leader


class LeaderSerializer(ModelSerializer):
    class Meta:
        model = Leader
        fields = ['id',
                  'name',
                  'lastname',
                  'type_of_document',
                  'document_number',
                  'email',
                  'address_of_residence',
                  'phone',
                  ]