from rest_framework import serializers
from .models import *

class FilmSerializer(serializers.Serializer):
    Title = serializers.CharField(max_length=100)
    Country = serializers.CharField(max_length=100)
    Language = serializers.CharField(max_length=100)
    Director = serializers.CharField(max_length=100)
    Writer = serializers.CharField(max_length=100)
    Actors = serializers.CharField(max_length=100)
    Actress = serializers.CharField(max_length=100)
    Genre = serializers.CharField(max_length=100)
    Type = serializers.CharField(max_length=100)
    Year = serializers.IntegerField()
    imdbRating = serializers.IntegerField()
    Runtime = serializers.IntegerField()

    def create(self,validate_data):
        return Film.objects.create(**validate_data)