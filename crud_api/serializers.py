from rest_framework import serializers
from .models import *


def century_2000(value):
    if value <2000:
        raise serializers.ValidationError('Movie should be 21th centurary')
        
        

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
    Year = serializers.IntegerField(validators=[century_2000])
    imdbRating = serializers.IntegerField()
    Runtime = serializers.IntegerField()

    def create(self,validate_data):
        return Film.objects.create(**validate_data)
    
    def update(self,instance,validated_data):
        print(instance.Title)
        instance.Title = validated_data.get('Title',instance.Title)
        print(instance.Title)
        instance.Country = validated_data.get('Country',instance.Country)
        instance.Language = validated_data.get('Language',instance.Language)
        instance.Writer = validated_data.get('Writer',instance.Writer)
        instance.Director = validated_data.get('Director',instance.Director)
        instance.Actors = validated_data.get('Actors',instance.Actors)
        instance.Actress = validated_data.get('Actress',instance.Actress)
        instance.Genre = validated_data.get('Genre',instance.Genre)
        instance.Type = validated_data.get('Type',instance.Type)
        instance.Year = validated_data.get('Year',instance.Year)
        instance.imdbRating = validated_data.get('imdbRating',instance.imdbRating)
        instance.Runtime = validated_data.get('Runtime',instance.Runtime)

        instance.save()
        return instance
    
    def validate_imdbRating(self,value):
        if value>=10:
            raise serializers.ValidationError("maximum imdb rating entered for the api")

        return value

    def validate(self,data):
        actors = data.get('Actors')
        actress = data.get("Actress")

        if actors == actress:
            raise serializers.ValidationError("actors and actress name are same")
        return data
    
