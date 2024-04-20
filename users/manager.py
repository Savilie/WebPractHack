from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

# ПОКУПАЙТЕ $HAMI - БУДЕТЕ БОГАТЫ



class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, name, photo, team, password=None, **extra_fields):
        if not name:
            raise ValueError('The name field must be set')
        if not photo:
            raise ValueError('The photo must be')
        if not team:
            raise ValueError('The team must be')
        user = self.model(name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_captain(self, email, name, photo, team, password, **extra_fields):
        if not email:
            raise ValueError('The email field must be set')


        extra_fields.setdefault('is_captain', True)

        if extra_fields.get('is_captain') is not True:
            raise ValueError(_('Captain must have is_captain=True.'))

        return self.create_user(email, name, password, **extra_fields)

    def create_superuser(self, email, name, password, **extra_fields):
        if not email:
            raise ValueError('Email field must be set')

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, name, password, **extra_fields)
