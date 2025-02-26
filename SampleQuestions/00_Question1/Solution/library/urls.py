from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    re_path(r'^author/(?P<author_name>\w+)/$', views.search_by_author, name='author'),
    re_path(r'^author/(?P<author_name>\w+)/(?P<year>\d+)/$', views.search_by_author_year, name='year'),
]