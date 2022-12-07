from django.contrib.auth.forms import UserCreationForm

from .models import User


class CreateUserForm(UserCreationForm):
    """Форма создания пользователя"""
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']