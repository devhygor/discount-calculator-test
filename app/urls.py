from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='form'),
    path('resultado/', views.form, name='resultado'),
]
