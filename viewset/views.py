from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


class InternModelViewSet(viewsets.ModelViewSet):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



class InternReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]


class InternViewSet(viewsets.ViewSet):

    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def show(self):
        print("****list*****")
        print("basename : ", self.basename)
        print("action : ", self.action)
        print("Detail : ", self.detail)
        print("Suffix : ", self.suffix)
        print("name : ", self.name)
        print("desc : ", self.description)

    def list(self,request):
        self.show()

        i = Intern.objects.all()
        s = InternSerializer(i,many=True)
        return Response(s.data)
    
    def retrieve(self,request,pk=None):
        self.show()
        id = pk
        if id is not None:
            i = Intern.objects.get(id=id)
            s=InternSerializer(i)
            return Response(s.data)
        return Response({'msg':'data not found'},status=status.HTTP_404_NOT_FOUND)

    def create(self,request):
        s =  InternSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response({'msg':f'id = {s.data["id"]} and name = {s.data["name"]} data created'},status=status.HTTP_201_CREATED)
        return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        id = pk
        i = Intern.objects.get(id=id)
        s = InternSerializer(i,data=request.data)
        if s.is_valid():
            s.save()
            return Response({'msg':f"{id} Data updated"},status=status.HTTP_205_RESET_CONTENT)
        return Response(s.errors,status=status.HTTP_304_NOT_MODIFIED)

    def partial_update(self,request,pk):
        id = pk
        i = Intern.objects.get(id=id)
        s = InternSerializer(i,data=request.data,partial=True)
        if s.is_valid():
            s.save()
            return Response({'msg':f'{id} partial updated'})
        return Response(s.errors,status=status.HTTP_304_NOT_MODIFIED)

    def destroy(self,request,pk):
        id = pk
        i = Intern.objects.get(id=id)
        i.delete()
        return Response({'msg':f'{id} Data deleted'},status=status.HTTP_410_GONE)