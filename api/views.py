from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.models import User
from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer