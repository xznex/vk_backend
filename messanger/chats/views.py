from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from chats.models import Chat, ChatMember, Message
from users.models import User
from django.views.decorators.csrf import csrf_exempt


@require_GET
def start_page(request):
    return render(request, "chats/index.html")


# 1. создать чат (минимальный набор полей: название, описание)
@require_POST
@csrf_exempt
def chat_create(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    creator_id = request.POST.get('creator_id')

    creator = get_object_or_404(User, id=creator_id)
    chat = Chat.objects.create(title=title, description=description, creator=creator)
    ChatMember.objects.create(chat=chat, member=creator)
    return JsonResponse(
        {
            'chat': {
                "title": chat.title,
                "created_at": chat.created_at.strftime('%d.%m.%Y %H:%M'),
                "username": chat.creator.username,
                "description": chat.description
            },
        }, json_dumps_params={'ensure_ascii': False}, status=201
    )


# 2. отредактировать чат по id (минимальный набор полей: название, описание)
@require_POST
@csrf_exempt
def chat_edit(request, chat_id):
    title = request.POST.get('title')
    description = request.POST.get('description')

    chat = get_object_or_404(Chat, id=chat_id)
    if title == chat.title or description == chat.description:
        return JsonResponse({'error': 'duplicate title or description'})
    if title:
        chat.title = title
    if description:
        chat.description = description
    chat.save()
    return JsonResponse(
        {
            'chat': {
                "title": chat.title,
                "created_at": chat.created_at.strftime('%d.%m.%Y %H:%M'),
                "username": chat.creator.username,
                "description": chat.description
            },
        }, json_dumps_params={'ensure_ascii': False}, status=201
    )


# 3. добавить участника в чат по id человека и id чата (минимальная проверка: то, что человек уже не добавлен в чат)
@require_POST
@csrf_exempt
def chat_add_user(request):
    user_id = request.POST.get('user_id')
    chat_id = request.POST.get('chat_id')

    chat = get_object_or_404(Chat, id=chat_id)
    user = get_object_or_404(User, id=user_id)
    if ChatMember.objects.filter(chat=chat, member=user).exists():
        return JsonResponse({'error': "user already added"})
    ChatMember.objects.create(chat=chat, member=user)
    return JsonResponse(
        {
            'chat_member': {
                "title": chat.title,
                "username": user.username
            }
        }, json_dumps_params={'ensure_ascii': False}
    )


# 4. удалить участника из чата по id человека и id чата
@require_POST
@csrf_exempt
def chat_delete_user(request):
    user_id = request.POST.get('user_id')
    chat_id = request.POST.get('chat_id')

    chat = get_object_or_404(Chat, id=chat_id)
    user = get_object_or_404(User, id=user_id)
    chat_member = get_object_or_404(ChatMember, chat=chat, member=user)
    chat_member.delete()
    return JsonResponse({'success': "user removed from chat"}, json_dumps_params={'ensure_ascii': False})


# 5. удалить чат по id
@require_POST
@csrf_exempt
def chat_delete(request):
    chat_id = request.POST.get('chat_id')

    chat = get_object_or_404(Chat, id=chat_id)
    chat.delete()
    return JsonResponse({'success': "chat deleted"}, json_dumps_params={'ensure_ascii': False})


# 13. получить информацию о чате по id чата
@require_GET
def chat_detail(request, pk):
    chat = get_object_or_404(Chat, id=pk)
    chat_out = {
       "id": pk,
       "title": chat.title,
       "description": chat.description,
       "created_at": chat.created_at.strftime('%d.%m.%Y %H:%M'),
       "creator": chat.creator.username,
       "is_group": chat.is_group
    },
    return JsonResponse({'chat': chat_out}, json_dumps_params={'ensure_ascii': False})


# 10. получить список всех чатов
@require_GET
def chat_list(request):
    chats = Chat.objects.all()
    chat_list = []
    for chat in chats:
        chat_list.append({
            "id": chat.id,
            "title": chat.title,
            "description": chat.description,
            "created_at": chat.created_at.strftime('%d.%m.%Y %H:%M'),
            "creator": chat.creator.username,
            "is_group": chat.is_group
        })
    return JsonResponse({'chats': chat_list}, json_dumps_params={'ensure_ascii': False})


@require_GET
def chats_by_user_id(request, user_id):
    user = get_object_or_404(User, id=user_id)
    chats = user.creator_chats.all()
    chat_list = []
    for chat in chats:
        chat_list.append({
            "id": chat.id,
            "title": chat.title,
            "description": chat.description,
            "created_at": chat.created_at.strftime('%d.%m.%Y %H:%M'),
            "creator": chat.creator.username,
            "is_group": chat.is_group
        })
    return JsonResponse({'chats': chat_list}, json_dumps_params={'ensure_ascii': False})


# 6. отправить сообщение по id чата
@require_POST
@csrf_exempt
def chat_send_message(request):
    chat_member_id = request.POST.get('chat_member_id')
    text = request.POST.get('text')

    chat_member = get_object_or_404(ChatMember, id=chat_member_id)
    message = Message.objects.create(chat=chat_member.chat, sender=chat_member, text=text)
    return JsonResponse(
        {
            'message': {
                "username": chat_member.member.username,
                "title": chat_member.chat.title,
                "sent_at": message.sent_at.strftime('%d.%m.%Y %H:%M'),
                "text": text
            }
        }, json_dumps_params={'ensure_ascii': False}
    )


# 7. отредактировать сообщение по id сообщения
@require_POST
@csrf_exempt
def message_edit(request):
    message_id = request.POST.get('message_id')
    text = request.POST.get('text')

    Message.objects.filter(id=message_id).update(text=text)
    return JsonResponse({'message': text}, json_dumps_params={'ensure_ascii': False})


# 8. пометить сообщение прочитанным по id сообщения
@require_POST
@csrf_exempt
def message_delivered(request):
    message_id = request.POST.get('message_id')

    message = get_object_or_404(Message, id=message_id)
    message.is_delivered = True
    message.save()
    return JsonResponse({'success': "message delivered"}, json_dumps_params={'ensure_ascii': False})


# 9. удалить сообщение по id сообщения
@require_POST
@csrf_exempt
def message_delete(request):
    message_id = request.POST.get('message_id')

    message = get_object_or_404(Message, id=message_id)
    message.delete()
    return JsonResponse({'success': "message deleted"}, json_dumps_params={'ensure_ascii': False})


@require_GET
def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    message_out = {
        "id": message.id,
        "chat": message.chat.title,
        "sender": message.sender.member.username,
        "is_delivered": message.is_delivered,
        "sent_at": message.sent_at.strftime('%d.%m.%Y %H:%M'),
        "text": message.text,
    },
    return JsonResponse({'message': message_out}, json_dumps_params={'ensure_ascii': False})


# 11. получить список сообщений по id чата
@require_GET
def messages_by_chat_id(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    messages = Message.objects.filter(chat=chat)
    message_list = []
    for message in messages:
        message_list.append({
            "id": message.id,
            "sender": message.sender.member.username,
            "is_delivered": message.is_delivered,
            "text": message.text,
            "sent_at": message.sent_at.strftime('%d.%m.%Y %H:%M'),
        })
    return JsonResponse({'messages': message_list}, json_dumps_params={'ensure_ascii': False})


# 12. получить информацию о пользователе по id
@require_GET
def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_info = {
        "id": user.id,
        "phone": user.phone,
        "bio": user.bio,
        "created_at": user.created_at.strftime('%d.%m.%Y %H:%M'),
    }
    return JsonResponse({'user': user_info}, json_dumps_params={'ensure_ascii': False})
