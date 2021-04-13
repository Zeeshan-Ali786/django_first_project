from django.urls import path
from . import views
from .views import Third

urlpatterns = [
    path('first', views.First),
    path('third', Third.as_view()),
    path('second', views.Second),
    path('template', views.temp),

    # path('class', Third.as_view())
]