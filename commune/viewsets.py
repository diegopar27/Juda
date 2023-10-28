from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import DjangoModelPermissions


from .models import Commune
from .Serializers import CommuneSerializer


class CommuneModelViewSet(ModelViewSet):
    serializer_class = CommuneSerializer
    queryset = Commune.objects.all()
    #permission_classes = [IsAuthenticated]
    permission_classes = (DjangoModelPermissions,)
    http_method_names = ['get', 'put', 'post', 'delete']