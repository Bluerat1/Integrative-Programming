from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from . managers import CustomUserManager
# Create your models here.
class User(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(_("email daw ni."), unique=True)
    id_number = models.IntegerField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "id_number"
    REQUIRED_FIELD = [
        "email"
    ]

    objects = CustomUserManager()

    def __str__(self):
        return self.id_number