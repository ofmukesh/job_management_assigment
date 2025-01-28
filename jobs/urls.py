from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import JobViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
