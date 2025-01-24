from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register_donor(request):
    if request.method == 'POST':
        # Extract form data from POST request
        full_name = request.POST.get('full-name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        blood_type = request.POST.get('blood-type')
        availability_date = request.POST.get('availability-date')
        address = request.POST.get('address')
        notes = request.POST.get('notes')

        # Log the data to the console
        print(f"Donor Details:\nName: {full_name}\nEmail: {email}\nPhone: {phone}\nBlood Type: {blood_type}\nAvailability: {availability_date}\nAddress: {address}\nNotes: {notes}")

        # Respond with a success message (could redirect or show success on the page)
        return JsonResponse({'message': 'Donor registered successfully!'})

    # For GET requests, render the HTML form
    return render(request, 'donorRegistration.html')