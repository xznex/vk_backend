from django.urls import path
from .views import UserRetrieveView


urlpatterns = [
    path('<int:pk>/', UserRetrieveView.as_view(), name="user_detail"),
]
