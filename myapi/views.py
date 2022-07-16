from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeroSerializer , PepleSerializer
from .models import Hero, Peple


class HeroViewset(viewsets.ModelViewSet):
    queryset  = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class PepleViewSet(viewsets.ModelViewSet):
    querys = Peple.objects.all().order_by('name')
    serializer_class = PepleSerializer


