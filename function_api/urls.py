from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/',data_api),
    path('',data_api),

    # path('',DataAPI.as_view(),name='function_api'),
    # path('<int:pk>/', DataAPI.as_view())
]
