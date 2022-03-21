from django.urls import path
from . import views

urlpatterns = [
  path('', views.taskList, name='tasks'),
  path('tasks', views.taskList2, name='tasks2'),
]
