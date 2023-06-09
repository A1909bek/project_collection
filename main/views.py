from django.shortcuts import render,get_object_or_404
from django.views import View
from projects.models import Project,Category

# Create your views here.



class IndexView(View):
    def get(self,request):
        projects = Project.objects.all()
        q = request.GET.get('q','')
        if q:
            projects = projects.filter(title__icontains=q)
        return render(request,'index.html',{'projects':projects})
    
    
class CategoryView(View):
    def get(self,request,category_name):
        category = get_object_or_404(Category,name=category_name)
        projects = Project.objects.filter(category=category)
        q = request.GET.get('q','')
        if q:
            projects = projects.filter(title__icontains=q)
        return render(request,'category.html',{'projects':projects,'category':category})
    
    
def for_all_pages(request):
    categories = Category.objects.all()
    
