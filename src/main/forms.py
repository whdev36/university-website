from django import forms
from .models import New, Category
from django.utils.safestring import mark_safe

class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ['title', 'content', 'author', 'image', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'Enter a title name'
        self.fields['title'].label = 'Title'
        self.fields['title'].help_text = ''
        self.fields['title'].label_suffix = ''

        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['placeholder'] = 'Enter a content text'
        self.fields['content'].label = 'Content'
        self.fields['content'].help_text = ''
        self.fields['content'].label_suffix = ''

        self.fields['author'].widget.attrs['class'] = 'form-control'
        self.fields['author'].widget.attrs['placeholder'] = ''
        self.fields['author'].label = 'Author'
        self.fields['author'].help_text = ''
        self.fields['author'].label_suffix = ''

        self.fields['image'].widget.attrs['class'] = 'form-control'
        # self.fields['image'].widget.attrs['placeholder'] = ''
        self.fields['image'].label = 'Image'
        self.fields['image'].help_text = ''
        self.fields['image'].label_suffix = ''

        self.fields['category'].widget.attrs['class'] = 'form-control'
        # self.fields['category'].widget.attrs['placeholder'] = ''
        self.fields['category'].label = 'Category'
        self.fields['category'].help_text = ''
        self.fields['category'].label_suffix = ''

    def as_div(self):
        output = []
        for field in self:
            output.append(f'<div class="form-group mb-3">{field.label_tag()}{field}</div>')
        return mark_safe('\n'.join(output))

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