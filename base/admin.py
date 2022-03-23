from django.contrib import admin
from .models import Task
from api.models import User

# Register your models here.
admin.site.register(User)
admin.site.register(Task)