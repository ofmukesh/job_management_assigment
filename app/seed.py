from django.core.management.base import BaseCommand
from freelancer.models import Freelancer
from jobs.models import Job
from applications.models import Application


class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **kwargs):
        # Create 5 freelancers
        for i in range(5):
            Freelancer.objects.create(
                name=f'Freelancer {i + 1}',
                email=f'freelancer{i + 1}@example.com'
                
            )

        # Create 5 jobs
        for i in range(5):
            Job.objects.create(
                title=f'Job {i + 1}',
                description=f'Description for job {i + 1}'
            )

        # Create 3 applications for each freelancer
        freelancers = Freelancer.objects.all()
        jobs = Job.objects.all()
        for freelancer in freelancers:
            for i in range(3):
                Application.objects.create(
                    freelancer=freelancer,
                    job=jobs[i % len(jobs)],
                    status='pending'
                )
