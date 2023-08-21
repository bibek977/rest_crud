from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='crud_home'),
    path('crud/',crud,name='crud'),
    path('crud_class/', CrudAPI.as_view()),
]
