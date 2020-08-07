from django.urls import path 
from . import views

urlpatterns = [
    path('putpoll/',views.putPoll,name="putPoll"),
    path('',views.index,name="index")
]