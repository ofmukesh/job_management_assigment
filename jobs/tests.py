from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Job

class JobAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.job = Job.objects.create(title="Test Job", description="Test Description")

    def test_get_jobs(self):
        response = self.client.get(reverse('job-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Job', response.data[0]['title'])

    def test_create_job(self):
        data = {'title': 'New Job', 'description': 'New Description'}
        response = self.client.post(reverse('job-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Job.objects.count(), 2)
        self.assertEqual(Job.objects.get(id=response.data['id']).title, 'New Job')
