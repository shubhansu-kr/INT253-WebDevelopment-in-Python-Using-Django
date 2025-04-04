from django.shortcuts import render
from .forms import MedicalForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def userform(request):
    if request.method == "POST":
        form = MedicalForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            return render(request, 'success.html', {"message": "Form submitted successfully!"})
        else:
            return render(request, 'userform.html', {'form': form, 'errors': form.errors})
    else:
        form = MedicalForm()

    return render(request, 'userform.html', {'form': form})