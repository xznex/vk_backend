from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=50, verbose_name="Имя")
    avatar = models.ImageField(null=True, blank=True, verbose_name="Автатар")
    phone = models.CharField(max_length=12, null=True, blank=True, verbose_name="Номер")
    bio = models.CharField(max_length=160, null=True, blank=True, verbose_name="Биография")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
