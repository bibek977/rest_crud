from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("throttling",InternApi,basename="throttling")

urlpatterns = [
    path('',include(router.urls)),
]
