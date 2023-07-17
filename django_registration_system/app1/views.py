from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            return HttpResponse('Password not matched')
        else:
            my_user=User.objects.create_user(username,email,pass1)
            my_user.save()
            print(username,email,pass1, pass2)
            return redirect('/login')
    return render(request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            return HttpResponse('Invalid Credentials')
        
    return render(request,'login.html')