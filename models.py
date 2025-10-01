from django.db import models

class myadmin(models.Model):
    myadmin_id = models.AutoField(primary_key=True)   # Auto increment primary key
    username = models.CharField(max_length=100, unique=True)  # Unique username
    password = models.CharField(max_length=255)    # Store password (hashed later)

    def __str__(self):
        return self.username
