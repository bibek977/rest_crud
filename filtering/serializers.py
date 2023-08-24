from rest_framework import serializers
from .models import *

class FilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = "__all__"