from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('internapi',InternViewSet,basename='intern')

urlpatterns = [
    path('',include(router.urls))
]
