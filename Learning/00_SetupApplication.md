# Setup Application

1. Start the Django project 
   1. `django-admin startproject Solution`
   2. `cd Solution`
   3. `python manage.py runserver` : This will launch the base start application on local host. 
2. Start an application within this project
   1. `django-admin startapp library`
   2. This will create an application directory within the Solution project
3. Link Library to Solution
   1. Open library directory and create `urls.py` file
      1. Add url patterns to this file
   2. Link this url file to the solution url.
   3. Add the following pattern in Solution's Urls.py 
      1. `path('library/', include('library.urls')),`
   4. Add this library application to the list of application in solution project
      1. Open `settings.py` in Solution project
      2. Add `library.apps.LibraryConfig`
   5. Create a basic template directory in library application
      1. Create `index.html` file in the templates
      2. Add a basic index file
   6. Add the index's req loader to the `views.py` file.
4. Start the server

Files 

Solution/urls.py : 
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', include('library.urls')),
]
```

Solution/settings.py : 
```
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'library.apps.LibraryConfig',
]
```

Library/urls.py
```
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

Library/views.py
```
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
```

Library/Template/index.html
```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hola Amigo</title>
</head>

<body>
    <header>
        <h1>Hola Amigo</h1>
        <p>How are you ?</p>
    </header>
</body>

</html>

```
