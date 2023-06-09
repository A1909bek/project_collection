from django import forms
from .models import Project

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','category','file','image']
        
    def save(self,request,commit=True):
        project = self.instance
        project.author = request.user
        super().save(commit)
        return project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'category')
        