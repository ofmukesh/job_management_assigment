import csv
from django.core.management.base import BaseCommand
from applications.models import Application
from jobs.models import Job
from freelancer.models import Freelancer


class Command(BaseCommand):
    help = 'Import applications from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str,
                            help='The path to the CSV file to be imported')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                job = Job.objects.get(id=row['job_id'])
                freelancer = Freelancer.objects.get(
                    user__email=row['freelancer_email'])
                Application.objects.create(
                    job=job,
                    freelancer=freelancer,
                    status=row['status']
                )
        self.stdout.write(self.style.SUCCESS(
            'Successfully imported applications'))
