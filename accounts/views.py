# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordResetForm
from django.contrib.auth import login, logout

# accounts/views.py
from .forms import CustomUserCreationForm
from django.contrib import messages

# accounts/views.py

def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            messages.success(request, 'Password reset link sent to your email')
            return redirect('accounts:login')
    else:
        form = PasswordResetForm()
    return render(request, 'accounts/reset_password.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('recipes:user_recipe_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('accounts:login')
