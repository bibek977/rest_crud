from rest_framework import serializers
from .models import *

# class MovieSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     country = serializers.CharField(max_length=50)
#     imdb = serializers.FloatField()
#     director = serializers.CharField(max_length=50)
#     runtime = serializers.IntegerField()

#     def create(self,validate_data):
#         return Movie.objects.create(**validate_data)
    

class MovieSerializer(serializers.ModelSerializer):
    # runtime = serializers.IntegerField(read_only=True)

    class Meta:
        model = Movie
        # fields = ['title','imdb','runtime']
        fields = '__all__'
        # read_only_fields = ['title','imdb']
        extra_kwargs = {'title':{'read_only':True}}