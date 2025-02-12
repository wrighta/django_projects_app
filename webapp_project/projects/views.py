from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required 
from .models import Project
from .forms import ProjectForm

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

@login_required 
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project.pk)  # Redirect to the project detail view
    else:
        form = ProjectForm(instance=project)

    return render(request, 'projects/project_edit.html', {'form': form, 'project': project})

from django.http import HttpResponseForbidden

@login_required 
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    
    # Check if the current user is allowed to delete this project
    #if project.creator != request.user:
     #   return HttpResponseForbidden("You are not allowed to delete this project.")
    
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    
    return render(request, 'projects/project_delete.html', {'project': project})



 
@login_required 
def project_add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            project.user = request.user  # Assign logged-in user 
            project.save() 
            return redirect('project_list')  # Redirect to the project list after saving the new project
    else:
        form = ProjectForm()

    return render(request, 'projects/project_add.html', {'form': form})
