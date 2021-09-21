from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms




class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)




class CreatNewUserForm (UserCreationForm):
    print('crete new user call')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2'] 


