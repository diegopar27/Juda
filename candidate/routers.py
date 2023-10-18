from rest_framework.routers import DefaultRouter
from candidate.views import CandidateModelViewSet

router_Candidate = DefaultRouter()

router_Candidate.register(prefix='Candidate', basename='Candidate', viewset=CandidateModelViewSet)