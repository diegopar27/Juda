from rest_framework.routers import DefaultRouter

from user.viewsets import UserViewSet

router_users = DefaultRouter()

router_users.register(prefix='users', basename='users', viewset=UserViewSet)