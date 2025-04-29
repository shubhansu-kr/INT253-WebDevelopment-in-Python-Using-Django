from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.userSignupView, name='signup'),
    path('login/', authViews.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', authViews.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboardView, name='dashboard'),
]
