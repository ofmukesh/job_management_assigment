from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Freelancer
from .serializers import FreelancerSerializer


class FreelancerViewSet(viewsets.ModelViewSet):
    queryset = Freelancer.objects.all()
    serializer_class = FreelancerSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated])
    def update_skills(self, request, pk=None):
        freelancer = self.get_object()
        serializer = self.get_serializer(
            freelancer, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def retrieve_freelancer(self, request, pk=None):
        freelancer = self.get_object()
        serializer = self.get_serializer(freelancer)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = {
            'user': {
                'first_name': request.data.get('name'),
                'email': request.data.get('email'),
                'password': request.data.get('password'),
                'username': request.data.get('email')
            },
            'skills': request.data.get('skills')
        }
        
        serializer = self.get_serializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except IntegrityError:
            return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
