from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contactFormView(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Normally save to DB or send email here
            return redirect("formSuccess")
    else:
        form = ContactForm()

    return render(request, "contactForm.html", {"form": form})

def formSuccessView(request):
    return render(request, "success.html")
