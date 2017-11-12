from django import forms
from . import models

class TaskForm(forms.ModelForm):
	class Meta:
		model = models.Task
		fields=('subject','description','reward','number_of_people','begin_date')

		widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'reward': forms.NumberInput(attrs={'class': 'form-control'}),
            'number_of_people': forms.NumberInput(attrs={'class': 'form-control'}),
            'begin_date': forms.DateInput(attrs={'class': 'form-control'}),
        }