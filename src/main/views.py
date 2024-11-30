from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import NewForm
from .models import New

# Homepage
def home(request):
    return render(request, 'home.html', {})

# New creation form view
@login_required
def create_new(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New successfully created!')
            return redirect('home') # Change to "news"
    else:
        form = NewForm()
    return render(request, 'new-form.html', {'form': form})

# All news page
def news(request):
    news = New.objects.all()
    return render(request, 'news.html', {'news': news})
