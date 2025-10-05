import json
from django.db import models
from django.contrib.postgres.fields import ArrayField

class PostTask(models.Model):
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
    ]
    ACTION_CHOICES = ['like', 'comment', 'follow', 'subscribe', 'share']

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    comments = ArrayField(models.TextField(), blank=True, default=list)
    actions = ArrayField(
        models.CharField(max_length=20),
        default=list,
        help_text="e.g., ['like', 'comment']"
    )
    frequency_seconds = models.PositiveIntegerField(default=300)
    max_executions = models.PositiveIntegerField(default=0)  # 0 = unlimited
    enabled = models.BooleanField(default=True)
    execution_count = models.PositiveIntegerField(default=0)
    created_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.platform}: {self.url[:50]}"