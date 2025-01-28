import csv
from django.core.management.base import BaseCommand
from job_management_assigment.models import Job, Freelancer

class Command(BaseCommand):
    help = 'Import jobs and freelancers from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to import')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['type'] == 'job':
                    Job.objects.create(
                        title=row['title'],
                        description=row['description']
                    )
                elif row['type'] == 'freelancer':
                    Freelancer.objects.create(
                        name=row['name'],
                        email=row['email']
                    )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
