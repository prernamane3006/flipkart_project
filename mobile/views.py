from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login as auth_login,logout,authenticate
from. models import*
from django.template import RequestContext

# Creat
def home(request):
    return render(request,'home.html')

def register(request):
        if request.method =="POST":
          first_name=request.POST.get("fname")
          last_name=request.POST.get("lname")
          email_id=request.POST.get("email")
          password=request.POST.get("password")
          user=User.objects.create_user(username=email_id,email=email_id,first_name=first_name,last_name=last_name,password=password)
          return render(request,'login.html')
        return render(request, 'register.html')

def login(request):
    if request.method=="POST":
        username=request.POST.get("email")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        
        print(user)
        if  user:
             auth_login(request,user)

        return render(request,'blog.html',{"message":"you have sucessfully login","user":request.user})
    return render(request,'login.html')

def blog_app(request):
     if request.method=="POST":
          title=request.POST.get("title")
          description=request.POST.get("description")
          created_date=request.POST.get("create_date")
          updated_at=request.POST.get("updated_at")
          Blog.objects.create(title=title,description=description,created_date=created_date,updated_at=updated_at,user=request.user)
          return render(request,"home.html")
     return render(request,"blog.html")     

  
  
