from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Application, Job, Freelancer


class ApplicationAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.job = Job.objects.create(
            title="Test Job", description="Test Description")
        self.freelancer = Freelancer.objects.create(
            name="Test Freelancer", email="test@example.com")
        self.application = Application.objects.create(
            job=self.job, freelancer=self.freelancer)

    def test_get_applications(self):
        response = self.client.get(reverse('application-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['job'], self.job.id)

    def test_create_application(self):
        data = {'job': self.job.id, 'freelancer': self.freelancer.id}
        response = self.client.post(
            reverse('application-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Application.objects.count(), 2)
        self.assertEqual(Application.objects.get(
            id=response.data['id']).job.id, self.job.id)
