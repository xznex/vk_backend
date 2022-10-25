from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


def start_page(request):
    if request.method == 'POST':
        return HttpResponse('405, Method Not Allowed', status=405)
    elif request.method == 'GET':
        return render(request, "chats/index.html")


def chat_list(request):
    if request.method == 'POST':
        return HttpResponse('405, Method Not Allowed', status=405)
    elif request.method == 'GET':
        chats = {
            "id": 5,
            "companion": "Abraham",
        }
        return JsonResponse(chats)


def chat_page(request, pk):
    if request.method == 'POST':
        return HttpResponse('405, Method Not Allowed', status=405)
    elif request.method == 'GET':
        chat = {
            "id": pk,
            "companion": "Abraham",
        }
        return JsonResponse(chat)


def chat_create(request):
    if request.method == 'GET':
        return HttpResponse('405, Method Not Allowed', status=405)
    elif request.method == 'POST':
        profile = {
            "id": 5,
            "name": "Abraham",
        }
        return JsonResponse(profile)
