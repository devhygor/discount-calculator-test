from django.urls import path
from . import views

app_name = 'calculadora'

urlpatterns = [
    path('', views.form, name='form'),
    path('resultado/', views.resultado, name='resultado'),
]
