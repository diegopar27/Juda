from rest_framework.routers import DefaultRouter
from commune.viewsets import CommuneModelViewSet

router_Commune = DefaultRouter()

router_Commune.register(prefix='commune', basename='commune', viewset=CommuneModelViewSet)