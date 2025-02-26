from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/', views.index, name='recipe_list'),
    path('<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('user/', views.user_profile, name='user_profile'),
]
