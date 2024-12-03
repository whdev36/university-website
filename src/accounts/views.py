from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

# Register
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # Get username data
            messages.success(request, 'Your account has been successfully created. Welcome!')
            return redirect('login') # Redirect to login
        else:
            messages.warning(request, 'Registration failed. Please check the details and try again.')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

# Users
@user_passes_test(lambda user: user.is_superuser)
def users(request):
    users = User.objects.all() # Get all users
    return render(request, 'accounts/users.html', {'users': users})

# Login
def login_user(request):
    # TODO: Create a custom login form
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None: # Check user
            login(request, user)
            messages.success(request, 'Welcome back! You have logged in successfully.')
            return redirect('home')
        else:
            messages.warning(request, 'Login failed. Please check your username and password.')
    return render(request, 'accounts/login.html', {})

# Logout
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have logged out successfully. See you next time!')
        return redirect('home')
    else:
        messages.warning(request, 'Logout failed. Please try again.')
        return redirect('home')

# Update
@login_required
def update_user(request):
    user = request.user
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('home') # TODO: Go to profile
        else:
            messages.warning(request, 'Failed to update your profile. Please try again.')
    else:
        form = RegisterForm(instance=user)
    return render(request, 'accounts/update.html', {'form': form})

# Delete
@login_required
def delete_user(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Your account has been successfully deleted. We\'re sorry to see you go.')
        return redirect('home')
    return render(request, 'accounts/delete.html', {})