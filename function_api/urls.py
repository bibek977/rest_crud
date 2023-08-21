from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='function_api'),
    path('<int:pk>',data_api)
]
