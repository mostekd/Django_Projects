from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Wpisz zadanie', 'class': 'form-control'})
        }
