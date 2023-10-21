from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Candidate
from .serializers import CandidateSerializer


class CandidateModelViewSet(ModelViewSet):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'put', 'post', 'delete']
