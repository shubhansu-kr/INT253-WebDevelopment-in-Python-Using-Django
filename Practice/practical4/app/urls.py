from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-book/', views.addBookView, name='addBook'),
    path('book-success/', views.bookSuccessView, name='bookSuccess'),
]