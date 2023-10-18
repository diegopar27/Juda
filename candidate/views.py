from rest_framework.viewsets import ModelViewSet

from .models import Candidate
from .serializers import CandidateSerializer


class CandidateModelViewSet(ModelViewSet):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()
    http_method_names = ['get', 'put', 'post', 'delete']
