from rest_framework import viewsets
from .models import Freelancer
from .serializers import FreelancerSerializer

class FreelancerViewSet(viewsets.ModelViewSet):
    queryset = Freelancer.objects.all()
    serializer_class = FreelancerSerializer
