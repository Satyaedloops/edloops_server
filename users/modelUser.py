from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string


class BucketUser(AbstractUser):
    userID = models.TextField(default=get_random_string(length=7), editable=False)
    is_verified = models.BooleanField(default=False)
    # profile_picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    inviteCode = models.TextField(default=get_random_string(length=4), editable=False)
    eligible = models.TextField(default=False, )
    courses = models.ManyToManyField(blank=True)