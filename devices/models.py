from django.db import models

class Device(models.Model):
    serial = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, default="Unnamed Device")
    platform = models.CharField(max_length=20, default="Android")
    status = models.CharField(max_length=20, default="Unknown")
    model = models.CharField(max_length=100, blank=True)
    android_version = models.CharField(max_length=20, blank=True)
    last_seen = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.serial})"