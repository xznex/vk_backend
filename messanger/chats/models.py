from django.db import models
from django.conf import settings


class Chat(models.Model):
    title = models.CharField(max_length=60, verbose_name="Название")
    avatar = models.ImageField(null=True, blank=True, verbose_name="Аватар")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="creator_chats",
        verbose_name="Создатель"
    )
    is_group = models.BooleanField(default=False, verbose_name="группа ли это")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"


class ChatMember(models.Model):
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name="chat_chatMembers",
        verbose_name="Чат"
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="member_chatMembers",
        verbose_name="Участник"
    )
    # is_creator = models.BooleanField(default=False, verbose_name="Создатель?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Участник чата"
        verbose_name_plural = "Участники чата"


class Message(models.Model):
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name="chat_messages",
        verbose_name="Чат"
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sender_messages",
        verbose_name="Отправитель"
    )
    is_delivered = models.BooleanField(default=False, verbose_name="Доставлено ли сообщение")
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    text = models.TextField(null=True, blank=True, verbose_name="Текст сообщения")

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-sent_at"]
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
