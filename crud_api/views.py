from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(csrf_exempt,name='dispatch')
class CrudAPI(View):
    def get(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            film = Film.objects.get(id=id)
            serializer = FilmSerializer(film)
            json_data = JSONRenderer().render(serializer.data)

            return HttpResponse(json_data, content_type="application/json")
        
        film = Film.objects.all()
        serializer = FilmSerializer(film,many=True)
        return JsonResponse(serializer.data, safe=False)
    

    def post(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = FilmSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            response = {'msg':"new api data created",
                        'res': 201}
            return JsonResponse(response,safe=False)

        return JsonResponse(serializer.errors,safe=False)
    

    def put(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        film = Film.objects.get(id=id)
        serializer = FilmSerializer(film,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': "data updated partially"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        return JsonResponse(serializer.errors,safe=False)
    

    def delete(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        film = Film.objects.get(id = id)
        film.delete()
        res = {'msg' : 'data deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')

def home(request):
    film = Film.objects.all()
    serializer = FilmSerializer(film,many=True)

    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def crud(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            film = Film.objects.get(id=id)
            serializer = FilmSerializer(film)
            json_data = JSONRenderer().render(serializer.data)

            return HttpResponse(json_data, content_type="application/json")
        
        film = Film.objects.all()
        serializer = FilmSerializer(film,many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = FilmSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            response = {'msg':"new api data created",
                        'res': 201}
            return JsonResponse(response,safe=False)

        return JsonResponse(serializer.errors,safe=False)
    
    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        film = Film.objects.get(id=id)
        serializer = FilmSerializer(film,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': "data updated partially"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        return JsonResponse(serializer.errors,safe=False)
        

    if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        film = Film.objects.get(id = id)
        film.delete()
        res = {'msg' : 'data deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')