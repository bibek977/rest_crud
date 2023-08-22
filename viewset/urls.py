from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('internapi',InternViewSet,basename='intern')
router.register("internapi_model",InternModelViewSet,basename="intern_model")
router.register('internapi_read',InternReadOnly,basename='intern_read')

urlpatterns = [
    path('',include(router.urls))
]
