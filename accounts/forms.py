from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=255,help_text='Required.')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        labels = {
            'username' : "UserName"
        }
        help_text = {
            'password1': "",
        }

    # def __init__(self, user, *args, **kwargs):
    #     super(UserForm,self).__init__(*args,**kwargs)
    #
    #     self.fields['password1'].help_text = None
