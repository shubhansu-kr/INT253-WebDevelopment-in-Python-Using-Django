from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def userSignupView(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # hash password
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'app/signup.html', {'form': form})

@login_required
def dashboardView(request):
    visitCount = request.session.get('visitCount', 0)
    visitCount += 1
    request.session['visitCount'] = visitCount

    response = render(request, 'app/dashboard.html', {'visitCount': visitCount})
    response.set_cookie('userName', request.user.username)
    return response
