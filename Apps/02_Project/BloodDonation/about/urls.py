from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register-donor/', views.register_donor, name='register_donor'),
]
