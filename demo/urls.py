from django.urls import path
from . import views
from .views import Third

urlpatterns = [
    path('first', views.First),
    path('s', views.Second),
    path('third', views.Third),
    path('class', Third.as_view())
]