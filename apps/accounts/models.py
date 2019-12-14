from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class AccountManager(UserManager):
    pass


class Accounts(AbstractUser):
    objects = AccountManager()

