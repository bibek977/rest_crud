from rest_framework import serializers
from .models import Intern

class InternSerializer(serializers.Serializer):
    # id=serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    phone = serializers.IntegerField()
    location = serializers.CharField(max_length=50)
    program = serializers.CharField(max_length=50)


    def create(self,validate_data):
        return Intern.objects.create(**validate_data)