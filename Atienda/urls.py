from django.urls import path
from Atienda.views import main
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('crud/', views.crud, name='crud'),
    path('clientesAdd/', views.ClientesAdd, name='clientesAdd'),  # Ajuste aquí
    path('listadoSQL/', views.listadoSQL, name='listadoSQL'),
    path('clientes_findEdit/<str:pk>/', views.clientes_findEdit, name='clientes_findEdit'),
    path('main/', views.main, name='main'),
    path('contacto/', views.contacto, name='contacto'),
    path('productos/', views.productos, name='productos'),  
    path('', main , name='main'),
    

]


