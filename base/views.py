from django.shortcuts import render
from django.http import HttpResponse

def taskList(request):
  return HttpResponse('To Do list')

def taskList2(request):
  return HttpResponse('To Do list')