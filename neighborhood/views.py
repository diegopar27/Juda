from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import DjangoModelPermissions
from .models import Neighborhood
from .serializers import NeighborhoodSerializer


class NeighborhoodModelViewSet(ModelViewSet):
    serializer_class = NeighborhoodSerializer
    queryset = Neighborhood.objects.all()
    #permission_classes = [IsAuthenticated]
    permission_classes = (DjangoModelPermissions,)
    http_method_names = ['get', 'put', 'post', 'delete']

