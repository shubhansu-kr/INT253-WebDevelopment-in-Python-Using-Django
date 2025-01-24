from django.shortcuts import render

# Create your views here.
def index(request): 
    return render(request, 'index.html')

def student_details(request):
    student = {
        'name': 'Satyam Thamkur',
        'roll_number': '59',
        'course': 'Computer Science',
        'marks': {'Math': 85, 'Physics': 94, 'Chemistry': 87}
    }
    
    return render(request, 'student.html', {'student': student})