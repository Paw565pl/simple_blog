from django.db import models
from django.conf import settings
from django_resized import ResizedImageField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = ResizedImageField(
        size=[300, 300], default="default.png", upload_to="profile_pics"
    )

    def __str__(self):
        return f"{self.user.username} Profile"
