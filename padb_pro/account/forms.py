from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CustomeUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"
