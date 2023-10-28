from rest_framework.serializers import ModelSerializer
from neighborhood.models import Neighborhood


class NeighborhoodSerializer(ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ['id',
                  'name_of_the_neighborhood',
                  'n_commune',
                 ]
