from django.db import models


class Freelancer(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    skills = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
