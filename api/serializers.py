from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=50)
    imdb = serializers.FloatField()
    director = serializers.CharField(max_length=50)
    runtime = serializers.IntegerField()

    def create(self,validate_data):
        return Movie.objects.create(**validate_data)