from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    #e-mail field if required
    #first_name=forms.CharField(max_length=30, required=True,)
    class Meta:
        model = User
        fields = ('username', 'password1','password2')  