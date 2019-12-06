from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, login_id, password):
        if not login_id:
            raise ValueError("User Must Have ID")

        user = self.model(
            login_id=login_id,
            plain_password=password,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login_id, password):
        user = self.create_user(
            login_id=login_id,
            password=password,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(
        primary_key=True,
    )
    login_id = models.CharField(
        max_length=50,
        unique=True,
    )
    name = models.CharField(
        max_length=10,
        null=True,
        blank=True,
    )
    phone = models.CharField(
        max_length=15,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        max_length=255,
        null=True,
        blank=True,
    )

    objects = UserManager()

    USERNAME_FIELD = 'login_id'
    REQUIRED_FIELDS = []

    def is_staff(self):
        return self.is_superuser

    def __str__(self):
        return str(self.login_id)