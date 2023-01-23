from django.shortcuts import render
from .models import Item
from rest_framework import viewsets
from .serializers import ItemSerializer


class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


