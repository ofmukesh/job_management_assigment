import csv
from django.core.management.base import BaseCommand
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
                Freelancer.objects.create(
                    name=row['name'],
                    email=row['email']
                )
        self.stdout.write(self.style.SUCCESS(
            'Successfully imported freelancers'))
