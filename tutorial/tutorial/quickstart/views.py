from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets # el uso de viewset mantiene la logica de la vista bien organizada
from quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API punto final que permite que los usuarios sean vistos o editados
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer