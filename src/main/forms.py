from django import forms
from .models import New

class NewForm(forms.ModelForm):
    class Meta:
        model = New # TODO: Change to "New"
        fields = ['title', 'content', 'author', 'image', 'category']