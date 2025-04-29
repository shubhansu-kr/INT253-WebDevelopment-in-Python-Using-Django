from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("contact/", views.contactFormView, name="contactForm"),
    path("contact/success/", views.formSuccessView, name="formSuccess"),
]