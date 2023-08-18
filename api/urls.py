from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="movie_api"),
    path('<int:pk>/',home_data),
    path('create_home/',create_home)
]
