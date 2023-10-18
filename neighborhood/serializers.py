from rest_framework.serializers import ModelSerializer
from neighborhood.models import Neighborhood, Neighborhood_leader


class NeighborhoodSerializer(ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ['id',
                  'name_of_the_neighborhood',
                 ]


class Neighborhood_leaderSerializer(ModelSerializer):
    class Meta:
        model = Neighborhood_leader
        fields = ['id',
                  'neighborhoods',
                  'leaders',
                  ]