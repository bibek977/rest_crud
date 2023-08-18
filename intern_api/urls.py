from django.urls import path
from .views import *

urlpatterns = [
    path('',intern_api,name="intern_api"),
    path("create_intern/",create_intern),
]
