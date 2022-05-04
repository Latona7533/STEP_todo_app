from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.CharField(max_length=30)
    created =models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

