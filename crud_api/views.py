from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

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