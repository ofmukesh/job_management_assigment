import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from freelancer.models import Freelancer


class Command(BaseCommand):
    help = 'Import freelancers from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str,
                            help='The path to the CSV file to be imported')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Create user first
                username = row['email'].split('@')[0]  # Use email prefix as username
                user = User.objects.create_user(
                    username=username,
                    email=row['email'],
                    first_name=row['name'].split()[0],
                    last_name=' '.join(row['name'].split()[1:]) if len(row['name'].split()) > 1 else ''
                )
                # Create freelancer profile
                Freelancer.objects.create(
                    user=user,
                    skills=row['skills']
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported freelancers'))
