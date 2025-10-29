# models.py
from django.db import models

class Dev(models.Model):
    dev_username = models.CharField(max_length=100, unique=True)
    dev_password = models.CharField(max_length=100)  # Store hashed password in production

    def __str__(self):
        return self.dev_username
