from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=15, unique=True)
    
    def __str__(self):
        return self.name

# linux so fast, it renders data from future 