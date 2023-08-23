from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register("auth",InternAPI,basename="auth")


urlpatterns = [
    path('',include(router.urls)),
    path('login/',include('rest_framework.urls', namespace="auth"))
]
