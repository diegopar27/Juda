from rest_framework.viewsets import ModelViewSet
from .models import Neighborhood_leader, Neighborhood
from .serializers import NeighborhoodSerializer, Neighborhood_leaderSerializer


class NeighborhoodModelViewSet(ModelViewSet):
    serializer_class = NeighborhoodSerializer
    queryset = Neighborhood.objects.all()
    http_method_names = ['get', 'put', 'post', 'delete']


class Neighborhood_leaderModelViewSet(ModelViewSet):
    serializer_class = Neighborhood_leaderSerializer
    queryset = Neighborhood_leader.objects.all()
    http_method_names = ['get', 'put', 'post', 'delete']
