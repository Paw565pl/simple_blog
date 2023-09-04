from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password1", "password2"]


class UserUpdateForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "image"]
