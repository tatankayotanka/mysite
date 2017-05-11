from django import forms
from django.contrib.auth.models import User
from .models import Task


class TaskForm(forms.ModelForm):
    """Creates the task creation model form"""
    class Meta:
        model = Task
        fields = ['title', 'assignee', 'description', 'progress', 'deadline']


class UserForm(forms.ModelForm):
    """Creates the user creation model form"""
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
