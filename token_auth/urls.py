from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from .auth import CustomAuthToken

router = DefaultRouter()

router.register("token_auth",InternAPI,basename="token_auth")


urlpatterns = [
    path('',include(router.urls)),
    path('login/',include('rest_framework.urls', namespace='token_auth')),
    # path('gettoken/', obtain_auth_token),
    path('gettoken/',CustomAuthToken.as_view())
]

# In Terminal write down the command for custom data to get Api key
# http POST http://127.0.0.1:8000/token_auth/gettoken/ username="admin" password="admin"


# To "GET" for token authentication
# http http://127.0.0.1:8000/token_auth/token_auth/ 'Authorization: Token 71ba18d61dfad60dea0fc5892d1219d5cc360a05 '

# To "POST"
# http -f POST http://127.0.0.1:8000/token_auth/token_auth/ name=bibekk phone=9800000 location=piluwa program=djangoReact 'Authorization: Token 71ba18d61dfad60dea0fc5892d1219d5cc360a05 '

# To "PUT"
# http PUT http://127.0.0.1:8000/token_auth/token_auth/5/ name=bibek phone=9819213927 location=piluwa program=django 'Authorization: Token 71ba18d61dfad60dea0fc5892d1219d5cc360a05 '

# To "DELETE"
# http DELETE http://127.0.0.1:8000/token_auth/token_auth/6/ 'Authorization: Token 71ba18d61dfad60dea0fc5892d1219d5cc360a05 '