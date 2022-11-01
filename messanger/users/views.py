# from django.shortcuts import render
from django.http import JsonResponse


def user_page(request, pk):
    page = [
        {
            "id": pk,
            "name": "Дженнифер Эшли",
            "avatar": "img_12-12-09",
            "sent_at": "15:52",
            "number": "+79099999999",
            "notifications": True,
            "block_user": False
        },
    ]
    return JsonResponse({'page': page}, json_dumps_params={'ensure_ascii': False})
