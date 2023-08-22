from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import GenericAPIView, ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny

class InternList(ListAPIView):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer

class InternListCreate(ListCreateAPIView):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer

class InternRetUpDe(RetrieveUpdateDestroyAPIView):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer

class InternLC(GenericAPIView, ListModelMixin,CreateModelMixin):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    

    
class InternRUD(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)   

