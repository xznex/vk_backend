from django.db import models
from application.settings import AUTH_USER_MODEL


class Chat(models.Model):
    name = models.CharField(max_length=60, verbose_name="Название")
    avatar = models.ImageField(null=True, blank=True, verbose_name="Аватар")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    creator = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Создатель")
    is_group = models.BooleanField(default=False, verbose_name="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"


class ChatMember(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name="Чат")
    member = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Участник")
    is_creator = models.BooleanField(default=False, verbose_name="Создатель?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Участник чата"
        verbose_name_plural = "Участники чата"


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name="Чат")
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    sender = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Отправитель")
    text = models.TextField(null=True, blank=True, verbose_name="Текст сообщения")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
