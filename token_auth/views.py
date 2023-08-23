from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

from .customauth import CustomAuthentication

class InternAPI(viewsets.ModelViewSet):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer

    # authentication_classes = [TokenAuthentication]
    authentication_classes = [CustomAuthentication]

    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]


    # IN url Section
    # http://127.0.0.1:8000/token_auth/token_auth/?username=Apeal91