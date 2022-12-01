# from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
