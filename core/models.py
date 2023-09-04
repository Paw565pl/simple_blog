from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    first_name = None
    last_name = None
    email = models.EmailField("email address", max_length=255, unique=True)
    image = ResizedImageField(
        size=[300, 300], default="default.png", upload_to="profile_pics"
    )

    def __str__(self) -> str:
        return self.username
