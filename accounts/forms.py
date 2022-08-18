from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

from accounts.models import User


class OrderForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    # first_name = forms.CharField(max_length=255)
    # last_name = forms.CharField(max_length=255)
    # username = forms.CharField(max_length=255)
    # email = forms.EmailField(max_length=255)
    # password = forms.CharField(max_length=250)
    # confirm_password = forms.CharField(max_length=250)
    #
    # class Meta:
    #     model = User
    #     fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password']
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
