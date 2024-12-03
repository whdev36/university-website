from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import mark_safe

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Create a new username'
        self.fields['username'].label = 'Username'
        self.fields['username'].help_text = ''
        self.fields['username'].label_suffix = ''

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email address'
        self.fields['email'].label = 'Email Address'
        self.fields['email'].help_text = ''
        self.fields['email'].label_suffix = ''

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'
        self.fields['first_name'].label = 'First Name'
        self.fields['first_name'].help_text = ''
        self.fields['first_name'].label_suffix = ''

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['last_name'].help_text = ''
        self.fields['last_name'].label_suffix = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Create a new password'
        self.fields['password1'].label = 'Create Password'
        self.fields['password1'].help_text = ''
        self.fields['password1'].label_suffix = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Re-enter password'
        self.fields['password2'].label = 'Confirm Password'
        self.fields['password2'].help_text = ''
        self.fields['password2'].label_suffix = ''

    def as_div(self):
        output = []
        for field in self:
            output.append(f'<div class="form-group mb-3">{field.label_tag()}{field}</div>')
        return mark_safe('\n'.join(output))