from django.urls import path
from .views import *


urlpatterns = [
    path('', start_page, name="chat_list"),
    path('chats/list/', chat_list, name="chat_list"),
    path('chats/<int:pk>/', chat_detail, name="chat_detail"),
    path('chats/create/', chat_create, name="chat_create"),
    path('chats/chat_edit/<int:chat_id>/', chat_edit, name="chat_edit"),
    path('chats/chat_create/', chat_create, name="chat_create"),
    path('chats/chat_add_user/', chat_add_user, name="chat_add_user"),
    path('chats/chat_delete_user/', chat_delete_user, name="chat_delete_user"),
    path('chats/chat_delete/', chat_delete, name="chat_delete"),
    path('chats/chat_detail/<int:pk>/', chat_detail, name="chat_detail"),
    path('chats/chat_list/', chat_list, name="chat_list"),
    path('chats/chats_by_user_id/<int:user_id>/', chats_by_user_id, name="chats_by_user_id"),
    path('chats/chat_send_message/', chat_send_message, name="chat_send_message"),
    path('chats/message_edit/', message_edit, name="message_edit"),
    path('chats/message_delivered/', message_delivered, name="message_delivered"),
    path('chats/message_delete/', message_delete, name="message_delete"),
    path('chats/message_detail/<int:message_id>/', message_detail, name="message_detail"),
    path('chats/messages_by_chat_id/<int:chat_id>/', messages_by_chat_id, name="messages_by_chat_id"),
    path('chats/user_detail/<int:user_id>/', user_detail, name="user_detail"),
]
