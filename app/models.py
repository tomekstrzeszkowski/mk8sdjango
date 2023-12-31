from django.contrib.auth.models import User
from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    details = models.CharField(max_length=500, blank=True)
    owner = models.ForeignKey(
        User, related_name="leads", on_delete=models.CASCADE, null=True
    )
    create_at = models.DateTimeField(auto_now_add=True)
