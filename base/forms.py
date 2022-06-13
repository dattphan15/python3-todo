# from django import forms
# from django.forms import ModelForm
from api.models import MyUser
# # from django.forms.widgets import EmailInput, PasswordInput
# from django.contrib.auth.forms import UserCreationForm

from django import forms
# from django.contrib.auth.models import User
# from getall.models import Profile
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# # Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()


class UserForm(forms.ModelForm):
# class UserForm(ModelForm):
    class Meta:
       model = MyUser
       fields = '__all__'
       fields = ['username', 'email', 'password'] # list of fields you want from model


# class UserForm(forms.ModelForm):
#    class Meta:
#        model = MyUser
#        fields = ['email',] # list of fields you want from model


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = MyUser
        fields = ['email',]


# class ProfileForm(forms.ModelForm):

#     class Meta:
#         model = Profile
#         fields = ['address', 'city', 'post']


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = MyUser
        fields = ("email", "first_name", "last_name")
        exclude = ("date_joined", "last_login")