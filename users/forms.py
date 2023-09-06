from django.forms import ModelForm, ValidationError
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth import get_user_model


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password1", "password2"]


class UserUpdateForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "image"]


class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data["email"]
        user = get_user_model().objects.filter(email=email).exists()
        if not user:
            raise ValidationError("There is no user with that email!")
        return email
