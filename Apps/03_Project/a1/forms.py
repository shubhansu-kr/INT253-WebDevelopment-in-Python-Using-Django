from django import forms
from django.core.exceptions import ValidationError
import datetime

def validate_future_date(value):
    if value < datetime.date.today():
        raise ValidationError("Appointment date cannot be in the past.")

class MedicalForm(forms.Form):
    patient_name = forms.CharField(max_length=100, required=True)
    age = forms.IntegerField(min_value=0, required=True)
    email = forms.EmailField(required=True)
    phone = forms.IntegerField(min_value=999999999, required=True)
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], required=True)
    symptoms = forms.CharField(widget=forms.Textarea, required=True)
    appointmentdate = forms.DateField(validators=[validate_future_date], required=True)
