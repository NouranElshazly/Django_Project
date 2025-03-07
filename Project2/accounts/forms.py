from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  
class UserRegistrationForm(UserCreationForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ("username", "image", "first_name", "last_name", "email")