from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, id_number, email, password, **extra_fields):
        if not email:
            raise ValueError(_("dili daw email imong gi input."))
        
        email = self.normalize_email(email)
        user = self.model(email=email, id_number=id_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user