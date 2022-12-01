from rest_framework import serializers
from .models import Chat, ChatMember, Message


class ChatMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatMember
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        chat = Chat.objects.create(**validated_data)
        ChatMember.objects.create(chat=chat, member=validated_data['creator'])
        return chat

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.is_group = validated_data.get('is_group', instance.is_group)
        instance.creator = validated_data.get('creator', instance.creator)
        instance.save()
        return instance

    class Meta:
        model = Chat
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
