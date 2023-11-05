from rest_framework.serializers import ModelSerializer
from commune.models import Commune


class CommuneSerializer(ModelSerializer):
    class Meta:
        model = Commune
        fields = ['id',
                  'name_commune',
                  ]
