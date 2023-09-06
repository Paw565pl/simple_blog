from typing import Any
from django.db.models import QuerySet, Model
from django.forms.models import BaseModelForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import get_user_model
from .forms import UserRegisterForm, UserUpdateForm, CustomPasswordResetForm


# Create your views here.
class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, f"Account created. You can now log in.")
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    template_name = "users/profile.html"
    success_url = reverse_lazy("profile")

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        return self.request.user

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, f"Your account has been updated.")
        return super().form_valid(form)


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    from_email = "passwordservice@simpleblog.com"
