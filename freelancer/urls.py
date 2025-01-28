from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import FreelancerViewSet

router = DefaultRouter()
router.register(r'freelancers', FreelancerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
