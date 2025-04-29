from django.shortcuts import render, redirect
from .forms import BookForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def addBookView(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookSuccess')  # named URL for success
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def bookSuccessView(request):
    return HttpResponse("Book added successfully!")