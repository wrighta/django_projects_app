from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Points to the templates folder
