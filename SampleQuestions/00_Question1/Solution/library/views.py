from django.shortcuts import render

# Create a hardcoded dictionary of books 


# Create your views here.
def index(request):
    return render(request, 'index.html')