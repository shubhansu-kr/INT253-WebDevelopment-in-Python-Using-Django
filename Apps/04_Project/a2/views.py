from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .form import EmployeeForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def employee_form_view(request, pk=None):
    if pk:
        employee = get_object_or_404(Employee, pk=pk)
    else:
        employee = None
    
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            print('1')
            form.save()
            print('2')
            return redirect('employee_list')  # Change to your actual success URL
    else:
        form = EmployeeForm(instance=employee)
    
    return render(request, 'employee_form.html', {'form': form})


def employee_list_view(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})
