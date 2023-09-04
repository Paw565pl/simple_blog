from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import get_user_model


# Create your views here.
def register(request):
    pass
    # if request.method == "POST":
    #     form = UserRegisterForm(request.POST)
    #     if form.is_valid():
    #         form.save()

    #         messages.success(request, f"Account created! You can now log in.")
    #         return redirect("login")
    # else:
    #     form = UserRegisterForm()
    # return render(request, "users/register.html", {"form": form})


# @login_required()
def profile(request):
    pass
    # user = request.user
    # if request.method == "POST":
    #     user_update_form = UserUpdateForm(request.POST, instance=user)
    #     profile_update_form = ProfileUpdateForm(
    #         request.POST, request.FILES, instance=user.profile
    #     )
    #     if user_update_form.is_valid() and profile_update_form.is_valid():
    #         user_update_form.save()
    #         profile_update_form.save()
    #         messages.success(request, f"Your account has been updated!")
    #         return redirect("profile")
    #     else:
    #         messages.error(
    #             request, f"Provided data does not meet the requirements!", "danger"
    #         )
    #         return redirect("profile")
    # else:
    #     (profile, _) = get_user_model.objects.get_or_create(user=user) #TODO: get or 404
    #     user_update_form = UserUpdateForm(instance=user)
    #     profile_update_form = ProfileUpdateForm(instance=profile)
    #     return render(
    #         request,
    #         "users/profile.html",
    #         {
    #             "user_update_form": user_update_form,
    #             "profile_update_form": profile_update_form,
    #         },
    #     )
