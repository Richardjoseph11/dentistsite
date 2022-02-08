from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('appointment/', views.appointment, name="appointment"),
    path('contact/', views.contact, name="contact"),
    path('pricing/', views.pricing, name="pricing"),
    path('service/', views.service, name="service"),
]
