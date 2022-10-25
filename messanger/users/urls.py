from django.urls import path
from .views import user_page


urlpatterns = [
    path('<int:pk>/', user_page, name="user_page"),
]
