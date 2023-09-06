from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordResetView
from .forms import UserRegisterForm, UserUpdateForm, CustomPasswordResetForm


# Create your views here.
class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, f"Account created! You can now log in.")
        return super().form_valid(form)


# @login_required() # FIXME: class based views
def profile(request):
    user = request.user
    if request.method == "POST":
        user_update_form = UserUpdateForm(request.POST, instance=user)
        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("profile")
        else:
            messages.error(
                request, f"Provided data does not meet the requirements!", "danger"
            )
            return redirect("profile")
    else:
        user_update_form = UserUpdateForm(instance=user)
        return render(
            request,
            "users/profile.html",
            {
                "user_update_form": user_update_form,
            },
        )


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    from_email = "passwordservice@simpleblog.com"
