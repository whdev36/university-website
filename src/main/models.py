from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.text import slugify
import os

def news_path(instance, filename):
    '''New image path.'''
    current_now = datetime.now()
    return os.path.join(f'news/{current_now.year}', filename)

# Category
class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        if not self.slug:
            self.slug = slugify(self.name.lower())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# New
class New(models.Model):
    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=news_path, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
