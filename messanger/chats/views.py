from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from chats.models import Chat, ChatMember, Message
from users.models import User


@require_GET
def start_page(request):
    return render(request, "chats/index.html")


@require_POST
def chat_create(request, title, description, creator_id):
    creator = get_object_or_404(User, id=creator_id)
    chat = Chat.objects.create(title=title, description=description, creator=creator)
    ChatMember.objects.create(chat=chat, member=creator)
    return JsonResponse({'chat': [chat.title, chat.created_at.strftime('%d.%m.%Y %H:%M'),
                                  chat.creator.username, chat.description]}, json_dumps_params={'ensure_ascii': False})


@require_POST
def chat_edit(request, chat_id, title=False, description=False):
    chat = get_object_or_404(Chat, id=chat_id)
    if title == chat.title or description == chat.description:
        return JsonResponse({'error': 'duplicate title or description'})
    if title:
        chat.title = title
    if description:
        chat.description = description
    chat.save()
    return JsonResponse({'chat': [chat.title, chat.created_at.strftime('%d.%m.%Y %H:%M'),
                                  chat.creator.username, chat.description]}, json_dumps_params={'ensure_ascii': False})


@require_POST
def chat_add_user(request, user_id, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    user = get_object_or_404(User, id=user_id)
    if ChatMember.objects.filter(chat=chat, member=user).first():
        return JsonResponse({'error': "user already added"})
    ChatMember.objects.create(chat=chat, member=user)
    return JsonResponse({'chat_member': [chat.title, user.username]}, json_dumps_params={'ensure_ascii': False})


@require_POST
def chat_delete_user(request, user_id, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    user = get_object_or_404(User, id=user_id)
    chat_member = get_object_or_404(ChatMember, chat=chat, member=user)
    chat_member.delete()
    return JsonResponse({'success': "user removed from chat"}, json_dumps_params={'ensure_ascii': False})


@require_POST
def chat_delete(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    chat.delete()
    return JsonResponse({'success': "chat deleted"}, json_dumps_params={'ensure_ascii': False})


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
    print(chat_list)
    return JsonResponse({'chats': chat_list}, json_dumps_params={'ensure_ascii': False})


@require_POST
def chat_send_message(request, chat_member_id, text):
    chat_member = get_object_or_404(ChatMember, id=chat_member_id)
    message = Message.objects.create(chat=chat_member.chat, sender=chat_member, text=text)
    return JsonResponse({'message': [chat_member.member.username, chat_member.chat.title,
                                     message.sent_at.strftime('%d.%m.%Y %H:%M'), text]},
                        json_dumps_params={'ensure_ascii': False})


@require_POST
def message_edit(request, message_id, text):
    Message.objects.filter(id=message_id).update(text=text)
    return JsonResponse({'message': text}, json_dumps_params={'ensure_ascii': False})


@require_POST
def message_delivered(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    message.is_delivered = True
    message.save()
    return JsonResponse({'success': "message delivered"}, json_dumps_params={'ensure_ascii': False})


@require_POST
def message_delete(request, message_id):
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


# @require_GET
# def chat_page(request, pk):
#     chat = [
#         {
#             "id": pk,
#             "name": "Дженнифер Эшли",
#             "avatar": "img_12-12-09",
#             "online": False,
#             "last_online": "15:38",
#             "messages": [
#                 {
#                     "message": "Lorem ipsum dolor sit amet",
#                     "sent_at": "14:59",
#                 },
#                 {
#                     "message": "Срочное совещание на третьем этаже!",
#                     "sent_at": "17:43",
#                 },
#             ]
#         },
#     ]
#     return JsonResponse({'chat': chat}, json_dumps_params={'ensure_ascii': False})
