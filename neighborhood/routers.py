from rest_framework.routers import DefaultRouter
from neighborhood.views import NeighborhoodModelViewSet, Neighborhood_leaderModelViewSet

router_Neighborhood = DefaultRouter()

router_Neighborhood.register(prefix='Barrio', basename='Barrio', viewset=NeighborhoodModelViewSet)

router_Neighborhood_leader = DefaultRouter()

router_Neighborhood_leader.register(prefix='liderBarrio', basename='liderBarrio', viewset=Neighborhood_leaderModelViewSet)