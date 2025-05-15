from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, id_number, email, password=None, **extra_fields):
        """
        Creates and returns a regular user with an email and password.
        """
        if not id_number:
            raise ValueError(_('The id_number must be set'))
        if not email:
            raise ValueError(_('The email must be set'))

        email = self.normalize_email(email)  # Normalize the email address
        user = self.model(id_number=id_number, email=email, **extra_fields)  # Create user instance
        user.set_password(password)  # Set password
        user.save(using=self._db)  # Save to the database
        return user

    def create_superuser(self, id_number, email, password=None, **extra_fields):
        """
        Creates and returns a superuser with the given id_number, email, and password.
        """
        extra_fields.setdefault('is_staff', True)  # Ensure the user is marked as staff
        extra_fields.setdefault('is_superuser', True)  # Ensure the user is a superuser
        extra_fields.setdefault('is_active', True)  # Ensure the user is active

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(id_number, email, password, **extra_fields)
