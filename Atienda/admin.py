from django.contrib import admin
from .models import Cliente
from .models import Productos, TipoProducto 

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Productos)
admin.site.register(TipoProducto)