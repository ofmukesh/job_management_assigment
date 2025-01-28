from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Freelancer


class FreelancerAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='newuser@example.com', password='testpass')
        self.freelancer = Freelancer.objects.create(
            user=self.user, skills='Python, Django')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_freelancer_success(self):
        url = reverse('freelancer-list')
        data = {
            'name': 'New User',
            'email': 'newuser2@example.com',
            'password': 'newpass',
            'skills': 'JavaScript, React'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Freelancer.objects.count(), 2)
        self.assertTrue(User.objects.filter(email='newuser2@example.com').exists())

    def test_create_freelancer_duplicate_email(self):
        url = reverse('freelancer-list')
        data = {
            'name': 'Test User',
            'email': 'newuser@example.com',  # Same as existing user
            'password': 'testpass',
            'skills': 'JavaScript, React'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_skills_success(self):
        url = reverse('freelancer-update-skills', args=[self.freelancer.id])
        data = {'skills': 'Python, Django, Flask'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.freelancer.refresh_from_db()
        self.assertEqual(self.freelancer.skills, 'Python, Django, Flask')

    def test_update_skills_unauthorized(self):
        self.client.force_authenticate(user=None)
        url = reverse('freelancer-update-skills', args=[self.freelancer.id])
        data = {'skills': 'Python, Django, Flask'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_freelancer_success(self):
        url = reverse('freelancer-retrieve-freelancer',
                      args=[self.freelancer.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['skills'], 'Python, Django')

    def test_retrieve_freelancer_unauthorized(self):
        self.client.force_authenticate(user=None)
        url = reverse('freelancer-retrieve-freelancer',
                      args=[self.freelancer.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
