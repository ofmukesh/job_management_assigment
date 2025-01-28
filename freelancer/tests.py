from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Freelancer


class FreelancerAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser@gmail.com', password='testpass', email='testuser@gmail.com', first_name='test user')
        self.freelancer = Freelancer.objects.create(
            user=self.user, skills="Python, Django")

    def test_get_freelancers(self):
        response = self.client.get(reverse('freelancer-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('testuser', response.data[0]['user']['username'])

    def test_create_freelancer(self):
        user = User.objects.create_user(username='newuser', password='newpass')
        data = {'user': user.id, 'skills': 'JavaScript, React'}
        response = self.client.post(
            reverse('freelancer-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Freelancer.objects.count(), 2)
        self.assertEqual(Freelancer.objects.get(
            id=response.data['id']).user.username, 'newuser')
