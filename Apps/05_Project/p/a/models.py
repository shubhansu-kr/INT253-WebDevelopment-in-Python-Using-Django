from django.core.exceptions import ValidationError
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    published_date = models.DateTimeField()

    def clean(self):
        if "spoiler" in self.content.lower():
            raise ValidationError("Content contains spoilers!")
