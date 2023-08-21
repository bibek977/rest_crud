from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework import status

from rest_framework.views import APIView



@api_view(['GET','POST',"PUT","PATCH","DELETE"])
def data_api(request,pk=None):
    if request.method == "GET":
        # id = request.data.get('id')
        id = pk
        if id is not None:
            intern = Intern.objects.get(id=id)
            serializer = InternSerializer(intern)
            return Response(serializer.data)
        intern = Intern.objects.all()
        serializer = InternSerializer(intern,many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = InternSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ({'msg' : 'new data posted'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "PUT":
        # id = request.data.get('id')
        id = pk
        i = Intern.objects.get(id=id)
        s = InternSerializer(i, data=request.data)
        if s.is_valid():
            s.save()
            return Response({'msg':f'data {id} updated completly'})

        return Response(s.errors)
    
    if request.method == "PATCH":
        # id = request.data.get('id')
        id = pk
        i = Intern.objects.get(id=id)
        s = InternSerializer(i, data=request.data, partial=True)
        if s.is_valid():
            s.save()
            return Response({'msg':f'data {id} updated partially'})

        return Response(s.errors)
    
    if request.method=="DELETE":
        # id = request.data.get("id")
        id = pk
        i = Intern.objects.get(id=id)
        i.delete()
        return Response({'msg' : f'item {id} deleted'})


class DataAPI(APIView):

    def get(self,request,pk=None,format=None):
        # id = request.data.get('id')
        id = pk
        if id is not None:
            intern = Intern.objects.get(id=id)
            serializer = InternSerializer(intern)
            return Response(serializer.data)
        intern = Intern.objects.all()
        serializer = InternSerializer(intern,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = InternSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ({'msg' : 'new data posted'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None,format=None):
        # id = request.data.get('id')
        id = pk
        i = Intern.objects.get(id=id)
        s = InternSerializer(i, data=request.data)
        if s.is_valid():
            s.save()
            return Response({'msg':f'data {id} updated completly'})

        return Response(s.errors)
    
    def patch(self,request,pk=None,format=None):
        # id = request.data.get('id')
        id = pk
        i = Intern.objects.get(id=id)
        s = InternSerializer(i, data=request.data, partial=True)
        if s.is_valid():
            s.save()
            return Response({'msg':f'data {id} updated partially'})

        return Response(s.errors)
    
    def delete(self,request,pk=None,format=None):

        # id = request.data.get("id")
        id = pk
        i = Intern.objects.get(id=id)
        i.delete()
        return Response({'msg' : f'item {id} deleted'})
