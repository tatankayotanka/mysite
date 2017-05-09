from django import forms
from django.contrib.auth.models import User

from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'assignee', 'description', 'progress', 'deadline']


#class UserForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)

    #class Meta:
        #model = User
        #fields = ['username', 'email', 'password']
