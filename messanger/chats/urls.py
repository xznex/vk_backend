from django.urls import path
from .views import *


urlpatterns = [
    path('', ChatListView.as_view(), name="chat_list"),
    path('<int:pk>/', ChatRUDView.as_view(), name="chat_detail"),
    path('create/', ChatCreateView.as_view(), name="chat_create"),
    path('edit/<int:pk>/', ChatRUDView.as_view(), name="chat_edit"),
    path('delete/<int:pk>/', ChatRUDView.as_view(), name="chat_delete"),
    path('user_chats/<int:user_id>/', UserChatsView.as_view(), name="user_chats"),
    path('add_user/', ChatMemberCreateView.as_view(), name="chat_add_user"),
    path('delete_user/<int:pk>/', ChatMemberDeleteView.as_view(), name="chat_delete_user"),
    path('message/send/', MessageSendView.as_view(), name="message_send"),
    path('message/edit/<int:pk>/', MessageRUDView.as_view(), name="message_edit"),
    path('message/delivered/<int:pk>', MessageRUDView.as_view(), name="message_delivered"),
    path('message/delete/<int:pk>/', MessageRUDView.as_view(), name="message_delete"),
    path('message/<int:pk>/', MessageRUDView.as_view(), name="message_detail"),
    path('messages/<int:chat_id>/', ChatMessagesView.as_view(), name="chat_messages"),
    path('user/<int:pk>/', UserRetrieveView.as_view(), name="user_detail"),
]
