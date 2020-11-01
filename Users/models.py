from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class AccountManager(BaseUserManager):
    def create_user(self, firstname, lastname, email, password):
        if not email:
            raise ValueError('Please specify valid email ID')

        email = self.normalize_email(email)
        user = self.model(firstname=firstname, lastname=lastname, email=email)

        user.set_password(password)
        user.save()

        return user


class Account(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    def get_full_name(self):
        return (self.firstname + ' ' + self.lastname)

    def __str__(self):
        return self.email