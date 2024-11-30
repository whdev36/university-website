from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

# Register
def register_user(request):
    # return HttpResponse('Register')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # Get username data
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
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