# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.room} reserved by {self.doctor} on {self.date} at {self.time}"