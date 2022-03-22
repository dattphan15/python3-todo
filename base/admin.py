from django.contrib import admin
from .models import Task
from account.models import Account

# Register your models here.
admin.site.register(Account)
admin.site.register(Task)