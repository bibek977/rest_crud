from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router = DefaultRouter()
router.register("json_token",InternApi,basename="json_token")

urlpatterns = [
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('refreshtoken/',TokenRefreshView.as_view(),name="token_refresh"),
    path('verifytoken/',TokenVerifyView.as_view(),name="token_verify"),
]

# To Get token
# http POST http://127.0.0.1:8000/json_token/gettoken/ username="Apeal91" password="user@123"

# To Verify Token
# http POST http://127.0.0.1:8000/json_token/verifytoken/ token="Key"

# To Refresh Token 
# http POST http://127.0.0.1:8000/json_token/refreshtoken/ refresh="Key(which is ref key)"


# To Get value
# http http://127.0.0.1:8000/json_token/json_token/ "Authorization: Bearer Key"

# To Post value
# http -f POST http://127.0.0.1:8000/json_token/json_token/ location=Piluwa name=bibek phone=9888888 program=software ""Authorization: Bearer Key""

# To Update value
# http PUT http://127.0.0.1:8000/json_token/json_token/id/ location=Piluwa program=software "Authorization: Bearer Key"

# To Delete value
# http DELETE http://127.0.0.1:8000/json_token/json_token/id/ "Authorization: Bearer Key"