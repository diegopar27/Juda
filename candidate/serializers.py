from rest_framework.serializers import ModelSerializer
from candidate.models import Candidate


class CandidateSerializer(ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id',
                  'name',
                  'last_name',
                  'type_of_document',
                  'document_number',
                  'email',
                  'address_of_residence',
                  'phone',
                  'political_party',
                  'Desired_position',
                  ]