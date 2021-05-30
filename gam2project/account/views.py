from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(requset):
    if requset.method == "POST":
        username = requset.POST['username']
        password = requset.POST['password']
        email = request.POST['email']
        if User.objects.filter(username = username).exists():
            return render(request, 'signup.html', {error:"이미 존재하는 사용자입니다. "})
        if password == requset.POST['passwordCheck']:
            user = User.objects.create_user(
                username, email, password = password
            )
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'error':"비밀번호가 일치하지 않습니다. "})
    else:
        return render(requset, 'signup.html')

def login(request):
    if request.method =="POST":
        username =request.POST['username']
        password =request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error':"사용자 이름 혹은 패스워드가 일치하지 않습니다."})
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def mypage(requset):
    return render(request, 'mypage.html')