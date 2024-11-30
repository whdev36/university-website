from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate, login, logout

# Register
def register_user(request):
    # return HttpResponse('Register')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # Get username data
            messages.success(request, f'Account created for {username}!')
            return redirect('login') # Redirect to login
        else:
            messages.warning(request, 'Something went wrong.')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# Users
@user_passes_test(lambda user: user.is_superuser)
def users(request):
    users = User.objects.all() # Get all users
    return render(request, 'accounts/users.html', {'users': users})

# Login
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None: # Check user
            login(request, user)
            messages.success(request, 'Login successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password!')
    return render(request, 'accounts/login.html', {})

# Logout
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('home')

# Update
@login_required
def update_user(request):
    user = request.user
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('home') # TODO: Go to profile
        else:
            messages.warning(request, 'Something went wrong.')
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'accounts/update.html', {'form': form})