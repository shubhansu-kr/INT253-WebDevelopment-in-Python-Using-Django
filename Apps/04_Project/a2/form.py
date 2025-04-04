from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'department', 'salary', 'email', 'number']
    
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['email'].widget.attrs['readonly'] = True
    
    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary < 10000:
            raise forms.ValidationError("Salary must be at least 10,000.")
        return round(salary, 2)
