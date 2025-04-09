from django.shortcuts import render, redirect
from .forms import BlogPostForm
from .models import BlogPost

def index(request):
    return render(request, 'index.html')

def success(request):
    return render(request, 'index.html')

def blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_blogs')  
    else:
        form = BlogPostForm()
    
    return render(request, 'blog.html', {'form': form})

def show_blogs(request):
    posts = BlogPost.objects.all().order_by('-published_date')  # latest first
    return render(request, 'show_blogs.html', {'posts': posts})
