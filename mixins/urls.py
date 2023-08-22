from django.urls import path
from .views import *

urlpatterns = [
    path('',InternLC.as_view()),
    path('<int:pk>/',InternRUD.as_view()),

    path("intern_list/",InternList.as_view()),
    
    path('intern_list_create/',InternListCreate.as_view()),
    path('intern_list_create/<int:pk>/',InternRetUpDe.as_view())
]
