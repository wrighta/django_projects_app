from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.forms import UserCreationForm 
from .models import CustomUser
from django.contrib import messages

def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def register(request): 
    if request.method == "POST": 
        form = UserCreationForm(request.POST) 
        if form.is_valid(): 
            user = form.save() 
            login(request, user) 
            return redirect("project_list")
    else: 
        form = UserCreationForm() 
    return render(request, "users/register.html", {"form": form}) 

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')  # Optional: Add a success message
            return redirect('projects:home')  # Redirect to the home page after login
        else:
            messages.error(request, 'Invalid username or password. Please try again.')  # Add an error message
            return redirect('users:login')  # Redirect back to the login page
    else:
        return render(request, 'users/login.html')

def user_logout(request): 
    logout(request) 
    return redirect("project_list") 