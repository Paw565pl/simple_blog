from django.forms import ModelForm, ValidationError, FileInput, ImageField
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth import get_user_model
from hcaptcha_field import hCaptchaField


class UserRegisterForm(UserCreationForm):
    hcaptcha = hCaptchaField()
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password1", "password2", "hcaptcha"]


class UserUpdateForm(ModelForm):
    image = ImageField(widget=FileInput)

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
