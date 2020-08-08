from django.urls import path 
from . import views

urlpatterns = [
    path('crudpoll/',views.crudPoll),
    path('',views.index)
]