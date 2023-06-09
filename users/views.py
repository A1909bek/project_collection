from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.views import View
from .forms import SignUpForm
from django.contrib import messages
from .models import CustomUser
# Create your views here.

class SignUpView(UserPassesTestMixin,View):
    
    def get(self,request):
        context = {
            'form':SignUpForm()
        }
        return render(request,'registration/signup.html',context)
    
    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your account is succesfully created.')
            return redirect('login')
        return render(request,'registration/signup.html',{'form':form})
        
    def test_func(self):
        user = self.request.user
        if user.is_authenticated:
            return False
        return True
    
class ProfileView(View):
    def get(self,request,username):
        user = get_object_or_404(CustomUser,username=username)
        context = {
            'customuser':user
        }
        return render(request,'profile.html',context)


class UpdateProfileView(LoginRequiredMixin,View):
    login_url = 'login'
    
    def get(self,request):
        form = UpdateProfileView(request.user)
        context = {
            'form':form
        }
        return render(request,'update_profile.html',context)
    
    def post(self,request):
        form = UpdateProfileView(instance=request.user,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account is successfully updated.')
            return redirect('profile',request.user)
        return render(request,'registration/signup.html',{'form':form})
            