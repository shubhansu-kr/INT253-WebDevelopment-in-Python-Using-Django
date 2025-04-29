from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submitData/', views.submitData, name='submitData'),
    path('getData/', views.getData, name='getData'),
    path('clearCookies/', views.clearCookies, name='clearCookies'),
]