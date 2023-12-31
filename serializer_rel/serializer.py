from rest_framework import serializers
from .models import *

class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True, read_only=True)
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
    # song = serializers.HyperlinkedIdentityField(view_name='song-detail')
    song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    class Meta:
        model = Singer
        fields = [ 'name','country', 'gender','song','age']


# class SongSerializer(serializers.ModelSerializer):
#     singer = serializers.StringRelatedField(read_only = True)
#     class Meta:
#         model = Song
#         fields = [ 'title' , 'singer' , 'year', 'duration']



class SongSerializer(serializers.HyperlinkedModelSerializer):
    singer = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Song
        fields = [ 'title' ,'url', 'singer' , 'year', 'duration']




class SingerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        exclude = ['id']
        

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    singer = SingerDetailSerializer(read_only = True)
    # singer = SingerSerializer(read_only = True)
    class Meta:
        model = Song
        fields = [ 'title' ,'url', 'singer' , 'year', 'duration']