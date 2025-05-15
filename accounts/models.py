from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# accounts/models.py
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from .managers import CustomUserManager

class User(AbstractUser, PermissionsMixin):
    username = None  # We don't need the `username` field
    email = models.EmailField(unique=True)
    id_number = models.IntegerField(unique=True)

    USERNAME_FIELD = 'id_number'  # Use `id_number` as the unique identifier
    REQUIRED_FIELDS = ['email']  # Make sure email is required

    objects = CustomUserManager()

    def __str__(self):
        return str(self.id_number)

class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class SensorReading(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    voltage = models.FloatField()
    current = models.FloatField()
    power = models.FloatField()
    energy = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reading at {self.timestamp} for {self.device.name}"
