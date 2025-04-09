from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('success/', views.success, name='success'),
    path('show_blogs/', views.show_blogs, name='show_blogs'),  # ⬅️ New route
    path('', views.index, name='index'),
]
