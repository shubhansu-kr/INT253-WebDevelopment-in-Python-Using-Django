from django.shortcuts import render, redirect
from .forms import BlogPostForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def success(request):
    return render(request, 'index.html')

def blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  
    else:
        form = BlogPostForm()
    
    return render(request, 'blog.html', {'form': form})
