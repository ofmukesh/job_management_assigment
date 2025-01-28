from django.db import models
from utils.common import STATUS_CHOICES
from freelancer.models import Freelancer
from jobs.models import Job


class Application(models.Model):
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.freelancer.full_name} - {self.job.title} - {self.status}"
