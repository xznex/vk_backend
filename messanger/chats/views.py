from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from chats.models import Chat, ChatMember, Message
from users.models import User


@require_GET
def start_page(request):
    return render(request, "chats/index.html")


# chat_create, message_create
# chat_detail, message_detail by ID
# chats_by_id - все чаты, которые есть у пользователя, messages_by_chat_id - все сообщения польза. по id чата
# chat_edit, message_edit by ID
# chat_delete, message_delete by ID


@require_POST
def chat_create(request, title, creator_id, avatar=None, is_group=False):
    creator = get_object_or_404(User, id=creator_id)
    Chat.objects.create(title=title, avatar=avatar, creator=creator, is_group=is_group)


@require_POST
def message_create(request, chat, sender, text, is_delivered=False):
    sender = get_object_or_404(User, id=sender)
    Chat.objects.create(chat=chat, sender=sender, text=text, is_delivered=is_delivered)


@require_GET
def chat_detail(request, pk):
    chat = get_object_or_404(Chat, id=pk)
    chat_out = {
       "id": pk,
       "title": chat.title,
       # "avatar": chat.avatar,
       "created_at": chat.created_at.strftime('%d.%m.%Y %H:%M'),
       "creator": chat.creator.username,
       "is_group": chat.is_group
   },
    return JsonResponse({'chat': chat_out}, json_dumps_params={'ensure_ascii': False})


@require_GET
def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    message_out = {
        "id": message.id,
        "chat": message.chat.title,
        "sender": message.sender.username,
        "is_delivered": message.is_delivered,
        "sent_at": message.sent_at.strftime('%d.%m.%Y %H:%M'),
        "text": message.text,
    },
    return JsonResponse({'message': message_out}, json_dumps_params={'ensure_ascii': False})


@require_GET
def chats_by_id(request, user_id):
    user = get_object_or_404(User, user_id)
    chats = user.creator_chats.all()
    return JsonResponse({'chats': chats}, json_dumps_params={'ensure_ascii': False})


@require_GET
def messages_by_chat_id(request, user_id, chat_id):
    user = get_object_or_404(User, user_id)
    chat = get_object_or_404(Chat, chat_id)
    messages = Message.objects.filter(sender=user, chat=chat)
    return JsonResponse({'messages': messages}, json_dumps_params={'ensure_ascii': False})


@require_POST
def chat_edit(request, chat_id, title=None, avatar=None):
    chat = get_object_or_404(Chat, chat_id)
    if title is not None:
        chat.update(title=title)
    if avatar is not None:
        chat.update(avatar=avatar)


@require_POST
def message_edit(request, message_id, text):
    message = get_object_or_404(Message, message_id)
    message.update(text=text)


@require_POST
def chat_delete(request, chat_id):
    chat = get_object_or_404(Chat, chat_id)
    chat.delete()


@require_POST
def message_delete(request, message_id):
    message = get_object_or_404(Message, message_id)
    message.delete()


@require_GET
def chat_list(request):
    chats = Chat.objects.all()
    chat_set = []
    for chat in chats:
        chat_set.append(
            {
                "id": chat.id,
                "title": chat.title,
                # "avatar": chat.avatar,
                "last_message": "Ты куда пропал?",
                "sent_at": "15:52",
                "number_of_unread_messages": 99,
                "viewed": False,
                "all": False
            }
        )
    return JsonResponse({'chats': chat_set}, json_dumps_params={'ensure_ascii': False})

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
