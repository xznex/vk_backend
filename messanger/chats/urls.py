from django.urls import path
from .views import start_page, chat_list, chat_page, chat_create


urlpatterns = [
    path('', start_page, name="chat_list"),
    path('chats/list/', chat_list, name="chat_list"),
    path('chats/<int:pk>/', chat_page, name="chat_page"),
    path('chats/create/', chat_create, name="chat_create"),
]
