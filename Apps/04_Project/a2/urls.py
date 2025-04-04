from django.urls import path

from . import views
from .views import employee_form_view

urlpatterns = [
    path('', views.index, name='index'),
    path('employee/add/', employee_form_view, name='employee_add'),
    path('employee/edit/<int:pk>/', employee_form_view, name='employee_edit'),
    path('employee/', views.employee_list_view, name='employee_list'),
]
