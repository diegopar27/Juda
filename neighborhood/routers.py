from rest_framework.routers import DefaultRouter
from neighborhood.views import NeighborhoodModelViewSet

router_Neighborhood = DefaultRouter()

router_Neighborhood.register(prefix='Barrio', basename='Barrio', viewset=NeighborhoodModelViewSet)
