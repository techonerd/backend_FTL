import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ssn = models.CharField(max_length=15, null=False, blank=False)
    job_title = models.CharField(max_length=100, blank=False, null=False)
    profile_picture = models.URLField(blank=True, null=True)
    tz = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    company = models.CharField(max_length=30, null=False, blank=False)
    password = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.username)


class Activity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(
        User, related_name="Activity", on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.user.username)
