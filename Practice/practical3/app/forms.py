from django import forms

class ContactForm(forms.Form):
    fullName = forms.CharField(max_length=50, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean_fullName(self):
        fullName = self.cleaned_data.get('fullName')
        if any(char.isdigit() for char in fullName):
            raise forms.ValidationError("Name cannot contain numbers.")
        return fullName
