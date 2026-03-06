from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Task


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-input', 'placeholder': 'Email address'
    }))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-input', 'placeholder': 'First name'
    }))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-input', 'placeholder': 'Last name'
    }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Confirm Password'})


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Password'})


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'category', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Task title...'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Description (optional)...', 'rows': 3}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'due_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
        }
