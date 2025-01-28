from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Application
from freelancer.models import Freelancer
from jobs.models import Job
from utils.common import STATUS_CHOICES


class ApplicationTests(TestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='admin123'
        )

        # Create test freelancer - removed experience field
        self.freelancer = Freelancer.objects.create(
            user=self.user,
            skills="Python, Django"
        )

        # Create test job
        self.job = Job.objects.create(
            title="Test Job",
            description="Test Description",
            required_skills="Python"
        )

        self.client = APIClient()

    def test_create_application_success(self):
        """Test successful application creation"""
        self.client.force_authenticate(user=self.user)
        data = {
            'freelancer': self.freelancer.id,
            'job': self.job.id,
            'status': STATUS_CHOICES[0][0]
        }
        response = self.client.post(reverse('application-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Application.objects.count(), 1)

    def test_create_application_unauthenticated(self):
        """Test application creation by unauthenticated user"""
        data = {
            'freelancer': self.freelancer.id,
            'job': self.job.id,
            'status': STATUS_CHOICES[0][0]
        }
        response = self.client.post(reverse('application-list'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_view_applications_with_filter(self):
        """Test viewing applications with freelancer filter"""
        self.client.force_authenticate(user=self.user)
        Application.objects.create(
            freelancer=self.freelancer,
            job=self.job
        )
        response = self.client.get(
            f"{reverse('application-view-applications')}?freelancer_id={self.freelancer.id}"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_view_applications_without_filter(self):
        """Test viewing all applications"""
        self.client.force_authenticate(user=self.user)
        Application.objects.create(
            freelancer=self.freelancer,
            job=self.job
        )
        response = self.client.get(reverse('application-view-applications'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_status_admin(self):
        """Test updating application status by admin"""
        self.client.force_authenticate(user=self.admin_user)
        application = Application.objects.create(
            freelancer=self.freelancer,
            job=self.job
        )
        new_status = STATUS_CHOICES[1][0]
        response = self.client.patch(
            reverse('application-update-status',
                    kwargs={'pk': application.pk}),
            {'status': new_status}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], new_status)

    def test_update_status_non_admin(self):
        """Test updating application status by non-admin user"""
        self.client.force_authenticate(user=self.user)
        application = Application.objects.create(
            freelancer=self.freelancer,
            job=self.job
        )
        new_status = STATUS_CHOICES[1][0]
        response = self.client.patch(
            reverse('application-update-status',
                    kwargs={'pk': application.pk}),
            {'status': new_status}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
