from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('dashboard')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Save last login time in cookie
            response = redirect('dashboard')
            response.set_cookie('last_login', str(timezone.now()))
            return response
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def dashboard_view(request):
    username = request.user.username
    last_login = request.COOKIES.get('last_login', 'First time login')
    return render(request, 'dashboard.html', {
        'username': username,
        'last_login': last_login
    })

def logout_view(request):
    logout(request)
    return redirect('login')
