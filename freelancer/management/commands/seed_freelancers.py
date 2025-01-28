from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from freelancer.models import Freelancer


class Command(BaseCommand):
    help = 'Seed the database with 5 freelancers'

    def handle(self, *args, **kwargs):
        freelancers_data = [
            {'username': 'freelancer1@example.com', 'email': 'freelancer1@example.com',
                'password': 'password1', 'skills': 'Python, Django'},
            {'username': 'freelancer2@example.com', 'email': 'freelancer2@example.com',
                'password': 'password2', 'skills': 'JavaScript, React'},
            {'username': 'freelancer3@example.com', 'email': 'freelancer3@example.com',
                'password': 'password3', 'skills': 'Java, Spring'},
            {'username': 'freelancer4@example.com', 'email': 'freelancer4@example.com',
                'password': 'password4', 'skills': 'C#, .NET'},
            {'username': 'freelancer5@example.com', 'email': 'freelancer5@example.com',
                'password': 'password5', 'skills': 'Ruby, Rails'},
        ]

        for data in freelancers_data:
            user = User.objects.create_user(
                username=data['username'], email=data['email'], password=data['password'])
            Freelancer.objects.create(user=user, skills=data['skills'])

        self.stdout.write(self.style.SUCCESS(
            'Successfully seeded the database with 5 freelancers'))
