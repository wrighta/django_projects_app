from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.forms import UserCreationForm 
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib import messages

def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('/login')  # Redirect to the login page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')  # Optional: Add a success message
            return redirect('projects')  # Redirect to the home page after login
        else:
            messages.error(request, 'Invalid username or password. Please try again.')  # Add an error message
            return redirect('users/login')  # Redirect back to the login page
    else:
        return render(request, 'login.html', {'form': form})
        #return render(request, 'users/login.html')

def user_logout(request): 
    logout(request) 
    return redirect("home") 