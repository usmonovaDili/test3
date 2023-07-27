from django.db import models
from django.utils import timezone


class Books(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    yozuvchi = models.CharField(max_length=40)
    publish_time = models.DateTimeField(auto_now=timezone.now)

    def __str__(self):
        return self.title