from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    count = forms.IntegerField(label='Count', min_value=0, max_value=100)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.isalpha():
            raise forms.ValidationError("Name should only contain letters.")
        return name