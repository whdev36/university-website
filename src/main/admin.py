from django.contrib import admin
from .models import Category, New # TODO: Change to "New"

# Register
admin.site.register(Category)

class NewAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']

admin.site.register(New, NewAdmin)