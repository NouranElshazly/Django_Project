from django.db import models
from django.contrib.auth.models import AbstractUser as DjangoUser

class User(DjangoUser):
    image = models.ImageField(upload_to="accounts/images/%Y/%m/%d/%h/%M/")

    def profile_picture(self):
        if self.image:
            return self.image.url
        else:
            return "https://www.shutterstock.com/image-vector/unknown-male-user-secret-identity-600nw-2055592583.jpg"
