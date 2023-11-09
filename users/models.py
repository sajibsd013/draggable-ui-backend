from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
credits = models.PositiveIntegerField(default=100)


USER_TYPE = (
    ('admin ', 'admin '),
    ('superadmin', 'superadmin'),
    ('user', 'user'),
)


# Create your models here
class MyUserManager(BaseUserManager):
    def create_user(self, username, password):
        """
        Creates and saves a User with the given username, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an username address')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username, date of
        birth and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(
        max_length=255,
        unique=True,
    )
    full_name = models.CharField(
        max_length=255,
    )
    email = models.CharField(
        max_length=255, null=True, blank=True
    )
    birthday = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    user_type = models.CharField(
        max_length=120, choices=USER_TYPE, default="user", )
    expiry_date = models.DateTimeField(null=True, blank=True)
    objects = MyUserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name_plural = "Users"
