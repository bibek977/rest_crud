from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class InternApi(viewsets.ModelViewSet):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]