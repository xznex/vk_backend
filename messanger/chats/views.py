from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseNotAllowed


@require_http_methods(["GET"])
def start_page(request):
    # if request.method == 'POST':
    #     return HttpResponse('405, Method Not Allowed', status=405)
    # elif request.method == 'GET':
    return render(request, "chats/index.html")


@require_http_methods(["GET"])
def chat_list(request):
    # if request.method == 'POST':
    #     return HttpResponse('405, Method Not Allowed', status=405)
    # elif request.method == 'GET':
    chats = [
        {
            "id": 1,
            "nickname": "Дженнифер Эшли",
            "avatar": "img_12-12-09",
            "last_message": "Ты куда пропал?",
            "dispatch_time": "15:52",
            "number_of_unread_messages": 99,
            "viewed": False,
            "all": False
        },
        {
            "id": 2,
            "nickname": "Общество целых бакалов",
            "avatar": "img_10-06-17",
            "last_message": "Ребят, сегодня без меня :(",
            "dispatch_time": "17:35",
            "number_of_unread_messages": 0,
            "viewed": True,
            "all": False
        },
    ]
    return JsonResponse({'chats': chats}, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def chat_page(request, pk):
    # if request.method == 'POST':
    #     return HttpResponse('405, Method Not Allowed', status=405)
    # elif request.method == 'GET':
    chat = [
        {
            "id": pk,
            "nickname": "Дженнифер Эшли",
            "avatar": "img_12-12-09",
            "online": False,
            "last_online": "15:38",
            "messages": [
                {
                    "message": "Lorem ipsum dolor sit amet",
                    "dispatch_time": "14:59",
                },
                {
                    "message": "Срочное совещание на третьем этаже!",
                    "dispatch_time": "17:43",
                },
            ]
        },
    ]
    return JsonResponse({'chat': chat}, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["POST"])
def chat_create(request):
    # if request.method == 'GET':
    #     return HttpResponse('405, Method Not Allowed', status=405)
    # elif request.method == 'POST':
    try:
        new_chat = [
            {
                "id": 1,
                "chat_id": 3,
            },
        ]
        return JsonResponse({'new_chat': new_chat})
    except 


# class CustomHTTPErrorsMiddleware(object):
#     def process_response(self, request, response):
#         if isinstance(response, HttpResponseNotAllowed):
#             return HttpResponse('405, Method Not Allowed', status=405)
#         return response


# def my_custom_page_not_found_view(self, request):
#     return HttpResponse('405, Method Not Allowed', status=405)
