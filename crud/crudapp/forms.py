from django import forms
from django.forms import ModelForm
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PublicTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name']  # lub ['name', 'category'] jeśli chcesz kategorię

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'deadline', 'category', 'is_done', 'attachment', 'public']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']