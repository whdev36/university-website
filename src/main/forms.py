from django import forms
from .models import News

class NewForm(forms.ModelForm):
    class Meta:
        model = News # TODO: Change to "New"
        fields = ['title', 'content', 'author', 'image', 'category']