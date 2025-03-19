from django.shortcuts import render
import re
from django.http import HttpResponse
import logging

# Create your views here.
def index(request):
    return render(request, 'index.html')

def userform(request):
    logger = logging.getLogger(__name__)

    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        symptom = request.POST.get('symptoms')
        date = request.POST.get('appointmentdate')

        errors = []

        if not patient_name:
            errors.append("Patient name is required.")
        if not age.isdigit() or not (0 <= int(age) <= 120):
            errors.append("Age must be a valid integer between 0 and 120.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("Email is not valid.")
        if not re.match(r"^\+?1?\d{9,15}$", phone):
            errors.append("Phone number is not valid.")
        if not symptom:
            errors.append("Symptom is required.")
        if not date:
            errors.append("Date is required.")

        if errors:
            return render(request, 'userform.html', {'errors': errors})

        logger.info(f"Patient Name: {patient_name}, Age: {age}, Email: {email}, Phone: {phone}, Symptom: {symptom}, Date: {date}")
        return HttpResponse("Success")
    
    return render(request, 'userform.html')