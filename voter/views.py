from rest_framework.viewsets import ModelViewSet

from .models import Voter
from .serializers import VoterSerializer


class VoterModelViewSet(ModelViewSet):
    serializer_class = VoterSerializer
    queryset = Voter.objects.all()
    http_method_names = ['get', 'put', 'post', 'delete']
