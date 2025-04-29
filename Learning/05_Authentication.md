# Authentication

## ✅ Scenario-based Question

> “Create a Django app where a user can sign up, log in, and access a dashboard that tracks how many times they’ve visited using sessions. The dashboard should only be visible after login.”

This will cover:

- User creation
- Login/Logout URLs
- Login required view
- Session management (count visits)
- Cookies (basic)

---

### 🔧 Step 1: Update `settings.py`

Add this if not present:

```python
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/login/'
```

---

### 📦 Step 2: URLs (`urls.py`)

```python
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.userSignupView, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboardView, name='dashboard'),
]
```

---

### 👤 Step 3: Signup Form (`forms.py`)

```python
from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
```

---

### 🧠 Step 4: Views (`views.py`)

```python
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignupForm

def userSignupView(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'app/signup.html', {'form': form})

@login_required
def dashboardView(request):
    visits = request.session.get('visits', 0)
    visits += 1
    request.session['visits'] = visits
    response = render(request, 'app/dashboard.html', {'visits': visits})
    response.set_cookie('user', request.user.username)
    return response
```

---

### 📄 Step 5: Templates

#### `signup.html`

```html
<h2>Signup</h2>
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sign up</button>
</form>
```

#### `login.html`

```html
<h2>Login</h2>
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>
```

#### `dashboard.html`

```html
<h2>Welcome {{ request.user.username }}</h2>
<p>You have visited this dashboard {{ visits }} times.</p>
<a href="{% url 'logout' %}">Logout</a>
```

---

## 🎯 Viva Q&A (Very Likely)

| Question | Answer |
|---------|--------|
| What is a session in Django? | Server-side mechanism to store user data between requests (e.g., visit count). |
| How are cookies used in Django? | Django sets session ID in a cookie; we can set custom cookies with `response.set_cookie`. |
| What does `@login_required` do? | Ensures only authenticated users can access the view. |
| What is `request.session['key']`? | A way to store/retrieve session data. |
| How is password stored? | Using `set_password`, Django hashes it before saving. |
| Difference between session and cookie? | Cookies are stored on the client; sessions are stored server-side, referenced by a session ID in a cookie. |

---
