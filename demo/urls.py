from django.urls import path
from . import views

urlpatterns = [
    path('first', views.First),
    path('second', views.Second),
]