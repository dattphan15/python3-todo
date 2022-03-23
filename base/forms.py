from django import forms
from api.models import User
# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()

class UserForm(forms.ModelForm):
   class Meta:
       model = User
       fields = ['username', 'email'] # list of fields you want from model
