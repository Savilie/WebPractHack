from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from teams.models import Team
from .manager import CustomUserManager

# ПОКУПАЙТЕ $HAMI - БУДЕТЕ БОГАТЫ


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True, verbose_name='Email адрес')
    name = models.CharField(max_length=255, verbose_name='Имя')
    desciprion = models.CharField(max_length=255, null=True)
    photo = models.TextField()
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE, related_name='user')
    is_staff = models.BooleanField(default=False)
    is_captain = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return self.name