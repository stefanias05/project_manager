from django import forms
from django.forms import TextInput, Textarea, Select, DateInput

from projects.models import Project
from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model= Task
        fields = [
            'title',
            'description',
            'status',
            'priority',
            'project',
            'deadline',
        ]

        widgets ={
            'title': TextInput(attrs={'class':'form-control','placeholder': 'Your task here'}),
            'description': Textarea(attrs={'class':'form-control','palceholder':'Describe your task',}),
            'status': Select(attrs={'class':'form-control'}),
            'priority': Select(attrs={'class':'form-control'}),
            'project': Select(attrs={'class':'form-control'}),
            'deadline': DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }

    def clean(self):
        cleaned_dates = self.cleaned_data
        print(cleaned_dates)
        deadline_task = cleaned_dates.get('deadline')
        deadline_project = cleaned_dates.get('project').end_date

        if deadline_task > deadline_project:
            msg = "The deadline task cannot be greater than the deadline project!"
            self._errors['deadline'] = self.error_class([msg])