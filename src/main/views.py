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
    return render(request, 'create-new.html', {'form': form})

# All news page
def news(request):
    news = New.objects.all()
    return render(request, 'news.html', {'news': news})

# New update view
def update_new(request, pk):
    new = New.objects.get(pk=pk)
    if request.method == 'POST':
        form = NewForm(request.POST, instance=new)
        if form.is_valid():
            form.save()
            # return redirect('new', pk=new.pk)
            return redirect('news')
    else:
        form = NewForm(instance=new)
    return render(request, 'update-new.html', {'form': form})

# New delete view
def delete_new(request, pk):
    new = New.objects.get(pk=pk)
    if request.method == 'POST':
        new.delete()
        messages.success(request, 'New deleted successfully!')
        return redirect('news')
    return render(request, 'delete-new.html', {'new': new})

