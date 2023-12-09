from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from django.forms import TextInput, EmailInput
from members.models import MemberUser
from django import forms


class NewAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your password'})


class MemberRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your username'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please choose your password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please confirm your password'})
        self.fields['username'] = forms.CharField(required=True, min_length=5, max_length=15)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your username'})

    class Meta:
        model = MemberUser
        fields = [
            'first_name',
            'last_name',
            'email',
            'position',
            'profile',
            'username'
        ]

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your valid email address '}),
            'position': TextInput(attrs={'class': 'form-control', 'placeholder': '"Analist IT","Frontend Dev" etc..'}),

        }

    def clean(self):
        """
        verific unicitatea pe adresei de email si validare format
        limita de caractere pe user: max 6 caractere

        """

        get_data = self.cleaned_data
        get_email = get_data.get('email')
        check_email = MemberUser.objects.filter(email=get_email)
        if check_email:
            msg = 'This email address already exists.'
            self._errors['email'] = self.error_class([msg])




class UserProfileForm(UserChangeForm):
    class Meta:
        model = MemberUser
        fields = [
            'username',
            'email',
            'position',
            'profile'
        ]

        widgets = {
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Update your email address '}),
            'position': TextInput(attrs={'class': 'form-control', 'placeholder': 'Update your position'}),
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': ' Change your username'}),
        }
