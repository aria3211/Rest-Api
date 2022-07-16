from django.urls import path, include
from rest_framework import routers
from .views import HeroViewset,PepleViewSet


router = routers.SimpleRouter()
router.register(r'herose',HeroViewset)
router.register(r'Pepole',PepleViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api_auth',include('rest_framework.urls',namespace='rest_framework')),
    # path('api_auth',include('rest_framework.urls',namespace='rest_framework')),
]
