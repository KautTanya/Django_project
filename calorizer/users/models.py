"""models for users"""
from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(unique=True, blank=False, null=False)

    def __str__(self):
        return f"Profile of {self.name}"
