from chats.serializers import ChatSerializer, ChatMemberSerializer, MessageSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

from chats.models import Chat, ChatMember, Message
from users.models import User


def login(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


class ChatCreateView(generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


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

    def create(self, request, *args, **kwargs):
        data = self.request.data
        chat = get_object_or_404(Chat, id=data.get('chat'))
        user = get_object_or_404(User, id=data.get('member'))

        if ChatMember.objects.filter(chat=chat, member=user).exists():
            return Response({'error': "user already added"}, status=401)

        ChatMember.objects.create(chat=chat, member=user)

        return Response({'status': 'success', 'message': 'a user has been added to the chat'}, status=201)


class ChatMemberDeleteView(generics.DestroyAPIView):
    queryset = ChatMember.objects.all()
    serializer_class = ChatMemberSerializer


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
