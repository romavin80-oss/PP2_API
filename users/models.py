from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    ADMIN = 'admin', _('administrator')
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name=_('Email'))
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER, verbose_name=_('Role'))
    first_name = models.CharField(max_length=30, verbose_name=_('First Name'), **NULLABLE)
    last_name = models.CharField(max_length=30, verbose_name=_('Last Name'), **NULLABLE)
    phone_number = models.CharField(max_length=20, verbose_name=_('Phone Number'), **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['last_name', 'first_name']
