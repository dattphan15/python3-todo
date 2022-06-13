from django.contrib import admin
from .models import Task
from api.models import MyUser

from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from api.models import MyUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = MyUser
    list_display = ["email",]
    # exclude = ("")


# Register your models here.
# admin.site.register(MyUser)
admin.site.register(MyUser, CustomUserAdmin)
admin.site.register(Task)