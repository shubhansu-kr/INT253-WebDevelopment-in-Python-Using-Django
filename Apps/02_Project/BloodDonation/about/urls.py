from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register-donor/', views.register_donor, name='register_donor'),
    re_path(r'^donor-details/(?P<donor_id>[0-9]+)/$', views.donor_details, name='donor_details'),
    re_path(r'^donation-date/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<slug>[\w-]+)/$', views.donation_date, name='donation_date'),
]

# You are building a Django application that handles blog posts. 
# You need to create a URL pattern using re_path() that matches the following conditions:
#  1. The URL should follow the format: /blog/yyyy/mm/dd/slug/
#  2.yyyy should be a 4-digit year (e.g., 2024).
#  3.mm should be a 2-digit month (01-12).
#  4.dd should be a 2-digit day (01-31).
#  5.slug should be a string containing letters, numbers, dashes, and underscores.
#  Write the Django urlpatterns entry for this
