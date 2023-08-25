from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *

class SingerAPI(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongAPI(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer