from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Job


class JobTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create test user and admin
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='admin123'
        )

        # Create test job
        self.job = Job.objects.create(
            title="Test Job",
            description="Test Description",
            required_skills="Python, Django"
        )

    def test_create_job_admin(self):
        """Test job creation by admin"""
        self.client.force_authenticate(user=self.admin_user)
        data = {
            'title': 'New Job',
            'description': 'New Job Description',
            'required_skills': 'Python, React'
        }
        response = self.client.post(reverse('job-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Job.objects.count(), 2)
        self.assertEqual(Job.objects.get(
            title='New Job').description, 'New Job Description')

    def test_create_job_non_admin(self):
        """Test job creation by non-admin user (should fail)"""
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'New Job',
            'description': 'New Job Description',
            'required_skills': 'Python, React'
        }
        response = self.client.post(reverse('job-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_job_list(self):
        """Test retrieving list of jobs"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('job-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_job_detail(self):
        """Test retrieving single job details"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            reverse('job-detail', kwargs={'pk': self.job.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Job')

    def test_update_job_admin(self):
        """Test updating job by admin"""
        self.client.force_authenticate(user=self.admin_user)
        data = {'title': 'Updated Job Title'}
        response = self.client.patch(
            reverse('job-detail', kwargs={'pk': self.job.pk}),
            data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Job.objects.get(
            pk=self.job.pk).title, 'Updated Job Title')

    def test_update_job_non_admin(self):
        """Test updating job by non-admin user (should fail)"""
        self.client.force_authenticate(user=self.user)
        data = {'title': 'Updated Job Title'}
        response = self.client.patch(
            reverse('job-detail', kwargs={'pk': self.job.pk}),
            data
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_job_admin(self):
        """Test deleting job by admin"""
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.delete(
            reverse('job-detail', kwargs={'pk': self.job.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Job.objects.count(), 0)

    def test_delete_job_non_admin(self):
        """Test deleting job by non-admin user (should fail)"""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(
            reverse('job-detail', kwargs={'pk': self.job.pk}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_job_unauthenticated(self):
        """Test accessing jobs while unauthenticated"""
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('job-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
