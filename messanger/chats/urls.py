from django.urls import path
from .views import *


urlpatterns = [
    path('chats/', ChatListView.as_view(), name="chat_list"),
    path('chats/<int:pk>/', ChatRUDView.as_view(), name="chat_detail"),
    path('chats/create/', ChatCreateView.as_view(), name="chat_create"),
    path('chats/edit/<int:pk>/', ChatRUDView.as_view(), name="chat_edit"),
    path('chats/delete/<int:pk>/', ChatRUDView.as_view(), name="chat_delete"),
    path('chats/user_chats/<int:user_id>/', UserChatsView.as_view(), name="user_chats"),
    path('chats/add_user/', ChatMemberCreateView.as_view(), name="chat_add_user"),
    path('chats/delete_user/<int:pk>/', ChatMemberDeleteView.as_view(), name="chat_delete_user"),
    path('chats/message/send/', MessageSendView.as_view(), name="message_send"),
    path('chats/message/edit/<int:pk>/', MessageRUDView.as_view(), name="message_edit"),
    path('chats/message/delivered/<int:pk>', MessageRUDView.as_view(), name="message_delivered"),
    path('chats/message/delete/<int:pk>/', MessageRUDView.as_view(), name="message_delete"),
    path('chats/message/<int:pk>/', MessageRUDView.as_view(), name="message_detail"),
    path('chats/messages/<int:chat_id>/', ChatMessagesView.as_view(), name="chat_messages"),
    path('chats/user/<int:pk>/', UserRetrieveView.as_view(), name="user_detail"),
]
