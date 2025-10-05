from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('operator', 'Operator'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='operator')
    last_seen = models.DateTimeField(null=True, blank=True)