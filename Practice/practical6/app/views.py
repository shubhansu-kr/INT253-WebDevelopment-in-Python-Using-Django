from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UserForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def submitData(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            count = form.cleaned_data['count']

            response = HttpResponseRedirect('/app/getData/')
            response.set_cookie('name', name)
            response.set_cookie('count', count)
            return response
        else:
            # Form not valid, render form with error messages
            return render(request, 'form.html', {'form': form})
    else:
        form = UserForm()
    return render(request, 'form.html', {'form': form})

def getData(request):
    name = request.COOKIES.get('name')
    count = request.COOKIES.get('count')

    if name is None or count is None:
        return render(request, 'message.html', {
            'message': 'No cookie data found. Please submit the form first.'
        })

    try:
        count = int(count) + 1
    except ValueError:
        count = 1

    response = render(request, 'message.html', {
        'name': name,
        'count': count,
        'message': f'Welcome back, {name}. Hit count incremented.'
    })
    response.set_cookie('count', count)
    return response

def clearCookies(request):
    response = redirect('submitData')  # Redirect to the form page after clearing
    response.delete_cookie('name')
    response.delete_cookie('count')
    return response