from django import forms
from account.models import Account
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm

# from django.contrib.auth import get_user_model
# User = get_user_model()

from django.conf import settings
User = settings.AUTH_USER_MODEL

# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()

# class RegisterForm(forms.ModelForm):
#     """
#     The default 
#     """

#     password = forms.CharField(widget=forms.PasswordInput)
#     password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['email']

#     def clean_email(self):
#         """
#         Verify email is available.
#         """
#         email = self.cleaned_data.get('email')
#         qs = Account.objects.filter(email=email)
#         if qs.exists():
#             raise forms.ValidationError("email is taken")
#         return email

#     def clean(self):
#         """
#         Verify both passwords match.
#         """
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         password_2 = cleaned_data.get("password_2")
#         if password is not None and password != password_2:
#             self.add_error("password_2", "Your passwords must match")
#         return cleaned_data

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    username = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', )


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email', 'password', 'is_active', 'is_admin']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]