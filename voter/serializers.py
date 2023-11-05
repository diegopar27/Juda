
from rest_framework.serializers import ModelSerializer
from voter.models import Voter


class VoterSerializer(ModelSerializer):
    class Meta:
        model = Voter
        fields = ['id',
                  'name',
                  'lastname',
                  'type_of_document',
                  'document_number',
                  'email',
                  'name_commune',
                  'name_neighborhood',
                  'phone',
                  'name_leader',
                  'voting_booth',
                  ]