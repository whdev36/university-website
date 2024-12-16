from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.text import slugify
import os
from django.core.validators import FileExtensionValidator

def news_path(instance, filename):
    '''New image path.'''
    current_now = datetime.now()
    return os.path.join(f'news/{current_now.year}', filename)

def videos_path(instance, filename):
    '''Post videos path.'''
    current_now = datetime.now()
    return os.path.join(f'videos/{current_now.year}', filename)

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

class Event(models.Model):
    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['-start_time']
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    location_url = models.URLField(blank=True, null=True)
    organizer = models.CharField(max_length=255)
    organizer_email = models.EmailField(blank=True, null=True)
    organizer_phone = models.CharField(max_length=25, blank=True, null=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Tag
class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        if not self.slug:
            self.slug = slugify(self.name.lower())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Post
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='posts')
    video = models.FileField(upload_to=videos_path,
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'mkv'])])
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes_count = models.PositiveIntegerField(default=0)
    views_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Post by {self.user.username} at {self.created_at}'