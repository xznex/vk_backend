# from django.shortcuts import render
from django.http import JsonResponse


def user_page(request, pk):
    chat = [
        {
            "pk": pk,
            "id": 5,
            "companion": "Abraham",
        },
    ]
    return JsonResponse({'chat': chat})
