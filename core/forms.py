from django import forms
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from .models import User


class UserChangeForm(BaseUserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = "__all__"
