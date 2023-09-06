from django.contrib import admin
from .models import User
from .forms import UserChangeForm


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username"]
    list_per_page = 20
    search_fields = ["username__istartswith"]
    form = UserChangeForm
