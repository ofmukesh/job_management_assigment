from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    required_skills = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
