from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Account created! You can now log in.")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


# @login_required()
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
