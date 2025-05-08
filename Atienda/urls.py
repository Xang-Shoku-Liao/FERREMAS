from django.urls import path
from Atienda.views import main
from . import views
from .views import iniciar_transaccion, confirmar_transaccion
from .front_enviar import webpay_form_view



urlpatterns = [
    path('index/', views.index, name='index'),
    path('crud/', views.crud, name='crud'),
    path('clientesAdd/', views.ClientesAdd, name='clientesAdd'),  # Ajuste aquí
    path('listadoSQL/', views.listadoSQL, name='listadoSQL'),
    path('clientes_findEdit/<str:pk>/', views.clientes_findEdit, name='clientes_findEdit'),
    path('main/', views.main, name='main'),
    path('contacto/', views.contacto, name='contacto'),
    path('productos/', views.productos, name='productos'),  
    path("form/", webpay_form_view, name="webpay_formulario"),
    path("api/webpay/iniciar/", iniciar_transaccion, name="iniciar_transaccion"),
    path("api/webpay/confirmar/", confirmar_transaccion, name="confirmar_transaccion"),
    
]


