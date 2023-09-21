from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Voter
from .serializers import VoterSerializer


class VoterModelViewSet(ModelViewSet):
    serializer_class = VoterSerializer
    queryset = Voter.objects.all()
    http_method_names = ['get', 'put', 'post', 'delete']
