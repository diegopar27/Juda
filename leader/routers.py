from rest_framework.routers import DefaultRouter
from leader.views import LeaderModelViewSet

router_Leader = DefaultRouter()

router_Leader.register(prefix='Leader', basename='Leader', viewset=LeaderModelViewSet)