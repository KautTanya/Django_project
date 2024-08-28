"""models for users"""
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=3)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    # phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"Profile of {self.first_name}"


class PhoneNumber(models.Model):
    profile = models.ForeignKey(UserProfile, related_name='phone_numbers', on_delete=models.CASCADE)
    number = models.CharField(max_length=15, blank=True)
