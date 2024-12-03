from django import forms
from .models import New, Category
from django.utils.safestring import mark_safe

class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ['title', 'content', 'author', 'image', 'category']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Enter a category name'
        self.fields['name'].label = 'Name'
        self.fields['name'].help_text = ''
        self.fields['name'].label_suffix = ''

        self.fields['slug'].widget.attrs['class'] = 'form-control'
        self.fields['slug'].widget.attrs['placeholder'] = 'Write the name of the slug'
        self.fields['slug'].label = 'Slug'
        self.fields['slug'].help_text = ''
        self.fields['slug'].label_suffix = ''

        def as_div(self):
            output = []
            for field in self:
                output.append(f'<div class="form-group mb-3">{field.label_tag()}{field}</div>')
            return mark_safe('\n'.join(output))