from chats.serializers import ChatSerializer, UserSerializer, ChatMemberSerializer, MessageSerializer
from rest_framework import generics

from chats.models import Chat, ChatMember, Message
from users.models import User


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
