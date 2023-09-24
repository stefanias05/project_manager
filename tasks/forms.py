from django import forms
from django.forms import TextInput, Textarea, Select, DateInput
from django.utils import timezone

from members.models import MemberUser
from projects.models import Project
from tasks.models import Task


class TaskForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(owner_id=user) | Project.objects.filter(
            team_members=user)

    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'status',
            'priority',
            'project',
            'deadline'
        ]

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Your task here'}),
            'description': Textarea(attrs={'class': 'form-control', 'palceholder': 'Describe your task'}),
            'status': Select(attrs={'class': 'form-control'}),
            'priority': Select(attrs={'class': 'form-control'}),
            'project': Select(attrs={'class': 'form-control'}),
            'deadline': DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }

#eroare aici ->object has no attribute 'end_date'
    # def clean(self):
    #     data = self.cleaned_data
    #     print(data)
    #     deadline_task = data.get('deadline')
    #     deadline_project = data.get('project').end_date
    #     if deadline_task>deadline_project:
    #         msg = "Deadline task cannot be greater than project deadline"
    #         self._errors['deadline'] = self.error_class([msg])





