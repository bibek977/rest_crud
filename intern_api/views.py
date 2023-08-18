from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import *
from .models import *
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt


def intern_api(request):
    intern = Intern.objects.all()
    s = InternSerializer(intern,many=True)
    return JsonResponse(s.data,safe=False)

@csrf_exempt
def create_intern(request):
    if request.method == "POST":
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = InternSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            response = {'message':201}

            return JsonResponse(response,safe=False)
        return JsonResponse(serializer.errors,safe=False)
        