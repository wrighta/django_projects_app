from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.forms import UserCreationForm 
from .models import CustomUser

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
    if request.method == "POST": 
        username = request.POST["username"] 
        password = request.POST["password"] 
        user = authenticate(request, username=username, password=password) 
        if user: 
            login(request, user) 
            return redirect("project_list") 
    return render(request, "users/login.html") 

def user_logout(request): 
    logout(request) 
    return redirect("project_list") 