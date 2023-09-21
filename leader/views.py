from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Leader
from .serializers import LeaderSerializer


class LeaderModelViewSet(ModelViewSet):
    serializer_class = LeaderSerializer
    queryset = Leader.objects.all()
    http_method_names = ['get', 'put', 'post', 'delete']
