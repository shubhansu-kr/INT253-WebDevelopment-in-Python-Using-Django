from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('detail', views.student_details, name='student details')
]
