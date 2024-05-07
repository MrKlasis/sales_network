from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=20, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=30, verbose_name='Фамилия', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    verbose_name = 'пользователь'
    verbose_name_plural = 'пользователи'
