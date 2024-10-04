from django.urls import path
from . import views

urlpatterns = [
    path('Monitor/', views.Monitor_list, name='Monitor_list'),
    path('Maquina/', views.Maquina_list, name='Maquina_list'),
    path('Clase/', views.Clase_list, name='Clase_list'),
]