from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('singer',SingerAPI,basename="singer")
router.register('song',SongAPI,basename="song")
router.register('album',AlbumAPI,basename="album")

urlpatterns = [
    path('', include(router.urls)),
    path('auth/',include('rest_framework.urls', namespace='rest_framwork'))
]
