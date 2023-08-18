from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.

def home(request):
    m = Movie.objects.all()
    s = MovieSerializer(m, many=True)
    json_data = JSONRenderer().render(s.data)
    return HttpResponse(json_data,content_type='application/json')

def home_data(request,pk):
    m = Movie.objects.get(id=pk)
    s = MovieSerializer(m)
    # json_data = JSONRenderer().render(s.data)
    # print(m)
    # print(s.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')

    return JsonResponse(s.data, safe=False)

@csrf_exempt
def create_home(request):
    if request.method=="POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = MovieSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response = {'message':201}
            return JsonResponse(response,safe=False)
        return JsonResponse(serializer.errors,safe=False)