from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import DjangoModelPermissions
from .models import Voter
from .serializers import VoterSerializer


class VoterModelViewSet(ModelViewSet):
    serializer_class = VoterSerializer
    queryset = Voter.objects.all()
    #permission_classes = [IsAuthenticated]
    permission_classes = (DjangoModelPermissions,)
    http_method_names = ['get', 'put', 'post', 'delete']


