from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.models import MyUser
from api.serializers import MyUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer