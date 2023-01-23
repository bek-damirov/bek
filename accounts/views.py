from django.shortcuts import render

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Create_user
from .serializers import Create_UserRegisterSerializer


class ProfileRegisterAPIView(viewsets.ModelViewSet):
    queryset = Create_user.objects.all()
    serializer_class = Create_UserRegisterSerializer


