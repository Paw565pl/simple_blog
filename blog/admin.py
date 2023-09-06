from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Post


# Register your models here.
# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_filter = ["author"]
    list_per_page = 20
    search_fields = ["title__istartswith"]
    autocomplete_fields = ["author"]
