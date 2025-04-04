from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'published_date']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        if content and 'django' not in content.lower():
            raise forms.ValidationError("Content must mention Django at least once 😄")
        return cleaned_data
