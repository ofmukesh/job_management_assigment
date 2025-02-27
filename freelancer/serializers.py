from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Freelancer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class FreelancerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Freelancer
        fields = ('id', 'user', 'skills', 'created_at')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(
            username=user_data['email'],
            email=user_data['email'],
            password=user_data['password'],
            first_name=user_data['first_name']
        )
        freelancer = Freelancer.objects.create(user=user, **validated_data)
        return freelancer
