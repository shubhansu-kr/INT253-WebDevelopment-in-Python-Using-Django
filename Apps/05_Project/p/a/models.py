from django.core.exceptions import ValidationError
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    published_date = models.DateTimeField()

    def clean(self):
        if "spoiler" in self.content.lower():
            raise ValidationError("Content contains spoilers!")

class Student(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    marks = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.roll_no})"

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="professors")

    def __str__(self):
        return f"{self.name} - {self.department.name}"


"""

---

python manage.py makemigrations a
python manage.py migrate

---

python manage.py shell

---

from a.models import Student, Department, Professor

# Create 5 students
Student.objects.create(roll_no=1, name="Alice", email="alice@example.com", marks=82.5)
Student.objects.create(roll_no=2, name="Bob", email="bob@example.com", marks=74.0)
Student.objects.create(roll_no=3, name="Charlie", email="charlie@example.com", marks=91.0)
Student.objects.create(roll_no=4, name="David", email="david@example.com", marks=69.5)
Student.objects.create(roll_no=5, name="Eve", email="eve@example.com", marks=88.0)

# Retrieve students with marks > 75
high_scorers = Student.objects.filter(marks__gt=75)
for student in high_scorers:
    print(student.name, student.marks)

# Create departments
cs = Department.objects.create(name="Computer Science", code="CS")
math = Department.objects.create(name="Mathematics", code="MATH")

# Add professors
Professor.objects.create(name="Dr. Smith", email="smith@uni.edu", department=cs)
Professor.objects.create(name="Dr. Allen", email="allen@uni.edu", department=cs)
Professor.objects.create(name="Dr. Rose", email="rose@uni.edu", department=math)
Professor.objects.create(name="Dr. Clark", email="clark@uni.edu", department=math)

# Get all professors in Computer Science
cs_profs = Professor.objects.filter(department__name="Computer Science")
for prof in cs_profs:
    print(prof.name, prof.email)

---

"""