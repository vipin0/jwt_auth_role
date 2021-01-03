from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            password=password,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            **extra_fields

        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# class CustomUserManager(BaseUserManager):
#     """
#     Custom user model where the email address is the unique identifier
#     and has an is_admin field to allow access to the admin app
#     """

#     def create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError(_("Users must have an email address"))
#         if not password:
#             raise ValueError(_("The password must be set"))
#         email = self.normalize_email(email)

#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_active', True)
#         extra_fields.setdefault('role', 1)

#         if extra_fields.get('role') != 1:
#             raise ValueError('Superuser must have role of Global Admin')
#         user = self.create_user(email, password, **extra_fields)
#         user.is_admin = True
#         user.is_superuser = True
#         return user
