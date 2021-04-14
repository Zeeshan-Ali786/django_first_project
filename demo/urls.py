from django.urls import path, include
from . import views
from .views import Third
from rest_framework import routers
from .views import StudentViewSet

router = routers.DefaultRouter()
router.register('students', StudentViewSet)

urlpatterns = [
    path('first', views.First),
    path('third', Third.as_view()),
    path('second', views.Second),
    path('template', views.temp),
    path('', include(router.urls)),

    # path('class', Third.as_view())
]