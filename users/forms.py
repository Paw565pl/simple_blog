from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings


# class UserRegisterForm(UserCreationForm):
#     # email = forms.EmailField(required=False)

#     class Meta:
#         model = settings.AUTH_USER_MODEL
#         fields = ("username", "email", "password1", "password2")


# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = settings.AUTH_USER_MODEL
#         fields = ("username", "email")


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = settings.AUTH_USER_MODEL
#         fields = ("image",)
