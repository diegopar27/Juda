from rest_framework.serializers import ModelSerializer
from commune.models import Commune
from neighborhood.serializers import NeighborhoodSerializer

class CommuneSerializer(ModelSerializer):
    neighborhoods = NeighborhoodSerializer(many=True, read_only=True)
    class Meta:
        model = Commune
        fields = ['id',
                  'name_commune',
                  'neighborhoods',
                  ]

