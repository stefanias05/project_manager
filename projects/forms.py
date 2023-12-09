from django import forms

from members.models import MemberUser
from projects.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:

        model = Project
        fields = ['name', 'description', 'start_date', 'end_date', 'status', 'priority']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the project name'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Describe the project', 'rows': 5}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={"class": 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'})
        }

    def clean(self):
        cleaned_date = self.cleaned_data

        start_date = cleaned_date.get('start_date')
        end_date = cleaned_date.get('end_date')
        if start_date > end_date:
            msg = " Start date cannot be greater than the end date "
            self._errors['start_date'] = self.error_class([msg])

        project_name = cleaned_date.get('name')
        check_name = Project.objects.filter(name=project_name)
        if check_name:
            msg = " This Project already exists !"
            self._errors['name'] = self.error_class([msg])


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date', 'status', 'priority']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the project name'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Describe the project', 'rows': 5}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={"class": 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'})
        }

    def clean(self):
        cleaned_date = self.cleaned_data

        start_date = cleaned_date.get('start_date')
        end_date = cleaned_date.get('end_date')
        if start_date > end_date:
            msg = " Start date cannot be greater than the end date "
            self._errors['start_date'] = self.error_class([msg])

        project_name = cleaned_date.get('name')
        check_name = Project.objects.filter(name=project_name)
        if check_name:
            msg = " This Project already exists !"
            self._errors['name'] = self.error_class([msg])


class ProjectAllocationMembersForm(forms.Form):
    team_members = forms.ModelMultipleChoiceField(
        queryset=MemberUser.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Select memebers",
        required=False
    )
