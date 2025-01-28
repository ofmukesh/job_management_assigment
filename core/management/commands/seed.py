from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from freelancer.models import Freelancer
from jobs.models import Job
from applications.models import Application
import random


class Command(BaseCommand):
    help = 'Seed database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database...')

        # Create 5 freelancers
        freelancers = []
        skills = ['Python', 'JavaScript', 'React', 'Django',
                  'Node.js', 'Angular', 'Vue.js', 'SQL', 'DevOps', 'AWS']

        for i in range(5):
            user = User.objects.create_user(
                username=f'freelancer{i+1}@example.com',
                email=f'freelancer{i+1}@example.com',
                password='password123',
                first_name=f'Freelancer {i+1}'
            )

            # Randomly select 3 skills for each freelancer
            freelancer_skills = ', '.join(random.sample(skills, 3))

            freelancer = Freelancer.objects.create(
                user=user,
                skills=freelancer_skills
            )
            freelancers.append(freelancer)
            self.stdout.write(f'Created freelancer: {user.email}')

        # Create 5 jobs
        jobs = []
        job_titles = [
            'Full Stack Developer',
            'Frontend Developer',
            'Backend Developer',
            'DevOps Engineer',
            'Software Architect'
        ]

        for i in range(5):
            # Randomly select 2-3 required skills for each job
            required_skills = ', '.join(
                random.sample(skills, random.randint(2, 3)))

            job = Job.objects.create(
                title=job_titles[i],
                description=f'We are looking for a {job_titles[i]} to join our team.',
                required_skills=required_skills
            )
            jobs.append(job)
            self.stdout.write(f'Created job: {job.title}')

        # Create 3 applications per freelancer
        for freelancer in freelancers:
            # Randomly select 3 jobs for each freelancer
            selected_jobs = random.sample(jobs, 3)

            for job in selected_jobs:
                Application.objects.create(
                    freelancer=freelancer,
                    job=job,
                    status='pending'
                )
                self.stdout.write(
                    f'Created application: {freelancer.user.first_name} -> {job.title}'
                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))
