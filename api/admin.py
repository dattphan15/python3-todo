# from django.contrib import admin
# from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# from .models import User


# class UserProfileInline(admin.StackedInline):
#     model = User
#     can_delete = False


# @admin.register(User)
# class UserAdmin(BaseUserAdmin):
#     fieldsets = '__all__'
#     # add_fieldsets = (
#     #     (None, {
#     #         'classes': ('wide',),
#     #         'fields': ('email', 'password1', 'password2'),
#     #     }),
#     # )
#     list_display = ('email', 'email', 'username', 'is_staff')
#     search_fields = ('email', 'email', 'username')
#     ordering = ('email',)
#     inlines = (UserProfileInline, )