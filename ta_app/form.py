from django import forms
from . import models
from django.contrib.auth.models import User

# -*- coding: utf-8 -*-

class TaskForm(forms.ModelForm):
	class Meta:
		model = models.Task
		fields=('subject','description','reward','number_of_people','begin_date')        
        
		widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'reward': forms.NumberInput(attrs={'class': 'form-control'}),
            'number_of_people': forms.NumberInput(attrs={'class': 'form-control'}),
            'begin_date': forms.DateInput(attrs={'class': 'form-control', 'id' : 'datepicker1', 'placeholder' : '2017-01-01'}),
        }

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','password','last_name','first_name','email') 
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }