from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import DjangoModelPermissions
from .models import Candidate
from .serializers import CandidateSerializer


class CandidateModelViewSet(ModelViewSet):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()
    #permission_classes = [IsAuthenticated]
    permission_classes = (DjangoModelPermissions,)
    http_method_names = ['get', 'put', 'post', 'delete']
