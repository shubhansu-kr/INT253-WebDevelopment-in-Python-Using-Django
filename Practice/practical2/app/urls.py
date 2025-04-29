from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail),
    path('author/<str:author_name>/', views.books_by_author),
    path('user/<str:user_name>/', views.books_by_user),
]