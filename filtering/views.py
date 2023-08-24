from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
import django_filters.rest_framework
from rest_framework.filters import SearchFilter

class FilmApi(viewsets.ModelViewSet):

    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


    # def get_queryset(self):
        
    #     user = self.request.user
    #     return Film.objects.filter(Director = user)

    # filter_backends = [DjangoFilterBackend]

    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = ['imdbRating', 'id']

    filter_backends = [SearchFilter]
    search_fields = ['Title', 'id']
    # search_fields = ['^Title', '=Country']

