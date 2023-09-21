from rest_framework.routers import DefaultRouter
from voter.views import VoterModelViewSet

router_Voter = DefaultRouter()

router_Voter.register(prefix='Voter', basename='Voter', viewset=VoterModelViewSet)