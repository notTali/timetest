from django.shortcuts import redirect, render
from .models import Project
from .forms import ProjectForm

# Create your views here.
def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'projects.html', context)

def project(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    context = {'project':project, "tags":tags}
    return render(request, 'project.html', context)

def addProject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(projects)
    context = {'form': form}
    return render(request, 'add-project.html', context)

def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect(projects)
    context = {'form': form}
    return render(request, 'add-project.html', context)
 
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect(projects)
    context = {"project":project}
    return render(request, 'delete.html', context)