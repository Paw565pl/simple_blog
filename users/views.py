from typing import Any
from django.db.models import QuerySet, Model
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import get_user_model
from .forms import UserRegisterForm, UserUpdateForm, CustomPasswordResetForm


# Create your views here.
class RegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")
    success_message = "Account created. You can now log in."


class ProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    template_name = "users/profile.html"
    success_url = reverse_lazy("profile")
    success_message = "Your account has been updated."

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        return self.request.user


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    from_email = "passwordservice@simpleblog.com"
