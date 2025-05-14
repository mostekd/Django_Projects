from django import forms
from .models import Task, Article

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Wpisz zadanie', 'class': 'form-control'})
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['url']
        widgets = {
            'url': forms.URLInput(attrs={'placeholder': 'https://pl.wikipedia.org/wiki/Przyk%C5%82ad', 'class': 'form-control'})
        }
