# Models

## ✅ Step 1: **Understanding Django Models**

### 🔹 What is a Model?
> A **model** is a Python class that defines the structure of your database table. Django translates this into SQL under the hood.

### 📄 Example — `models.py`

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publishedDate = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
```

### 🧠 Viva Questions:
- **Q: What is a model in Django?**  
  A: It's a Python class that maps to a database table and defines fields/columns.

- **Q: What is `models.CharField` used for?**  
  A: It's used for storing short text strings (e.g., names, titles).

- **Q: What does `ForeignKey` do?**  
  A: It creates a relationship between two models (many-to-one).

- **Q: What does `__str__` method do?**  
  A: It defines how the object is shown in Django Admin or shell (a readable name).

---

## ✅ Step 2: **Create and Apply Migrations**

### 🔹 What is a Migration?
> It's Django’s way of propagating changes made to your models into the database schema.

### 🧪 Commands:

```bash
python manage.py makemigrations
```
> Creates migration files based on your model changes.

```bash
python manage.py migrate
```
> Applies those changes to the database (creates tables).

### 🧠 Viva Questions:
- **Q: What is the difference between `makemigrations` and `migrate`?**  
  A: `makemigrations` creates migration files; `migrate` applies them to the DB.

- **Q: Where are migration files stored?**  
  A: Inside the `migrations/` folder in your app.

- **Q: What does an initial migration do?**  
  A: Creates the first version of database tables for your models.

---

## ✅ Step 3: **Registering Models in Django Admin**

### 📝 `admin.py`

```python
from django.contrib import admin
from .models import Author, Book

admin.site.register(Author)
admin.site.register(Book)
```

Now run the server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/admin` after creating a superuser:

```bash
python manage.py createsuperuser
```

### 🧠 Viva Questions:
- **Q: Why register models in `admin.py`?**  
  A: So that they are visible and manageable via the admin panel.

- **Q: What is Django Admin?**  
  A: A built-in interface for managing models and data.

---

## ✅ Step 4: **Working with Django ORM in Shell**

### 🔹 Django Shell:

```bash
python manage.py shell
```

### 🔹 Insert Data

```python
from app.models import Author, Book
from datetime import date

author1 = Author.objects.create(name='J.K. Rowling', bio='British author')
book1 = Book.objects.create(
    title='Harry Potter',
    publishedDate=date(1997, 6, 26),
    author=author1,
    price=299.99
)
```

### 🔹 Read Data

```python
Book.objects.all()
Author.objects.filter(name='J.K. Rowling')
```

### 🔹 Update Data

```python
author1.bio = 'Famous British author'
author1.save()
```

### 🔹 Delete Data

```python
Book.objects.get(title='Harry Potter').delete()
```

### 🧠 Viva Questions:
- **Q: What is ORM?**  
  A: Object-Relational Mapping — a way to interact with DB using Python classes and methods.

- **Q: How to insert data using ORM?**  
  A: `Model.objects.create()` or instantiate and call `.save()`.

- **Q: How to filter records?**  
  A: Using `Model.objects.filter(condition)`.

---

## ✅ Step 5: **Foreign Key Relationship**

```python
author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

### 🔹 Explanation:
- Links a book to an author.
- If the author is deleted, the books are also deleted (due to `CASCADE`).

### 🧠 Viva Questions:
- **Q: What does `on_delete=models.CASCADE` mean?**  
  A: Deletes all related child records if the parent is deleted.

- **Q: Can a book have multiple authors in this model?**  
  A: No, each book links to one author only. Use `ManyToManyField` for that.

---

## ✅ Step 6: **Users, Groups, and Permissions**

In Admin:
- Create new **users**
- Create **groups** like "Editors"
- Assign **permissions** (add, change, delete, view)

### 🧠 Viva Questions:
- **Q: How are permissions managed in Django?**  
  A: Through the admin panel using users and groups.

- **Q: Can we assign a model to a group?**  
  A: No, we assign permissions (on models) to groups.

- **Q: What’s the purpose of a superuser?**  
  A: Full access to the admin and all models.

---

## ✅ Step 7: **Database Configuration**

In `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # default DB
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### For PostgreSQL (if needed):

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bookstore',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Install the required package:

```bash
pip install psycopg2-binary
```

### 🧠 Viva Questions:
- **Q: Which database does Django use by default?**  
  A: SQLite

- **Q: How can we change the database engine?**  
  A: Modify the `DATABASES` dictionary in `settings.py`.

---
