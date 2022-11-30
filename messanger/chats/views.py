from chats.serializers import ChatSerializer, UserSerializer, ChatMemberSerializer, MessageSerializer
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import generics

from chats.models import Chat, ChatMember, Message
from users.models import User


def login(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


class ChatCreateView(generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


# if Chat.creator.filter(id=request.user.id).exists():
# 		ChatMember.objects.create(chat=chat, user=user)
# 		return JsonResponse()
class ChatRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class ChatListView(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class UserChatsView(generics.ListAPIView):
    serializer_class = ChatSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Chat.objects.filter(creator__id=user_id)


class ChatMemberCreateView(generics.CreateAPIView):
    queryset = ChatMember.objects.all()
    serializer_class = ChatMemberSerializer


class ChatMemberDeleteView(generics.DestroyAPIView):
    queryset = ChatMember.objects.all()
    serializer_class = ChatMemberSerializer


class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MessageRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageSendView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class ChatMessagesView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        return Message.objects.filter(chat__id=chat_id)


# def add_user(self, chat_id, user_id):
#     chat = get_object_or_404(Chat, id=chat_id)
#     user = get_object_or_404(User, id=user_id)
#     if Chat.objects.get(id=user_id).creator.is_owner:
#         ChatMember.objects.create(chat=chat, user=user)
#         return JsonResponse()
#     return JsonResponse({'error': 'Only admin can add chat members'}, status=403)
