"""
URL configuration for rest_crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('intern_api/',include('intern_api.urls')),
    path('crud_api/',include("crud_api.urls")),
    path('function_api/',include('function_api.urls')),
    path('mixins_api/',include('mixins.urls')),
    path('viewset/',include('viewset.urls')),
    path("auth_api/", include('auth_api.urls')),
    path("token_auth/", include('token_auth.urls')),
    path('json_token/',include('json_token.urls')),
    path('throttling/',include('throttling.urls')),
    path('filtering/',include('filtering.urls')),
    path('pagination/',include('pagination.urls')),
    path('serializer_rel/', include('serializer_rel.urls')),
]
