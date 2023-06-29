

from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from posts.views import home

# Create your views here.

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['repeat']:
            print("비번"+request.POST['password'])
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            
            auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print("로그인 성공")
            return redirect('posthome')
        else :
            return render(request, 'bad_login.html')
    else:
        return render(request, 'login.html')

def badlogin(request):
    return render(request, 'bad_login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')