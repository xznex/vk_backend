from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST


@require_GET
def start_page(request):
    return render(request, "chats/index.html")


@require_GET
def chat_list(request):
    chats = [
        {
            "id": 1,
            "name": "Дженнифер Эшли",
            "avatar": "img_12-12-09",
            "last_message": "Ты куда пропал?",
            "sent_at": "15:52",
            "number_of_unread_messages": 99,
            "viewed": False,
            "all": False
        },
        {
            "id": 2,
            "name": "Общество целых бакалов",
            "avatar": "img_10-06-17",
            "last_message": "Ребят, сегодня без меня :(",
            "sent_at": "17:35",
            "number_of_unread_messages": 0,
            "viewed": True,
            "all": False
        },
    ]
    return JsonResponse({'chats': chats}, json_dumps_params={'ensure_ascii': False})


@require_GET
def chat_page(request, pk):
    chat = [
        {
            "id": pk,
            "name": "Дженнифер Эшли",
            "avatar": "img_12-12-09",
            "online": False,
            "last_online": "15:38",
            "messages": [
                {
                    "message": "Lorem ipsum dolor sit amet",
                    "sent_at": "14:59",
                },
                {
                    "message": "Срочное совещание на третьем этаже!",
                    "sent_at": "17:43",
                },
            ]
        },
    ]
    return JsonResponse({'chat': chat}, json_dumps_params={'ensure_ascii': False})


@require_POST
def chat_create(request):
    new_chat = [
        {
            "id": 1,
            "chat_id": 3,
        },
    ]
    return JsonResponse({'new_chat': new_chat})
