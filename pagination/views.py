from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .custompage import *

class FilmApi(viewsets.ModelViewSet):

    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    pagination_class = MyPagePagination