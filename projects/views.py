from django.shortcuts import render,redirect,get_object_or_404
from .forms import NewProjectForm,ProjectForm
from django.contrib.auth.decorators import login_required
from .models import Project,Category
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def new_project(request):
    if request.method == 'GET':
        form = NewProjectForm()
        context = {
            'form':form
        }
        return render(request,'new_project.html',context)
    elif request.method == 'POST':
        form = NewProjectForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save(request=request)
            messages.success(request,'Succesfully Created')
            return redirect('main:index')
        return render(request,'new_project.html',{'form':form})

def project_detail(request,project_id):
    project = get_object_or_404(Project,id=project_id)
    context = {
        'project':project
    }
    return render(request,'project_detail.html',context)
    
            
