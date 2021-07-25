from django.db import models
from django.contrib.auth.models import User
import datetime

class Grocery(models.Model):
    name = models.CharField(max_length = 256)
    quantity = models.CharField(max_length = 128)
    status = models.IntegerField(default=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    def __str__(self):
        return f"{self.name}"