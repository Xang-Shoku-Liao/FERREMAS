from django.db import models


# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    celular = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
class Productos(models.Model):
    id_produ        = models.AutoField(db_column = 'idProdu', primary_key=True)
    nombre_producto = models.CharField(max_length=50)
    id_tipo         = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='idTipo', null=True)
    precio          = models.IntegerField()
    foto            = models.ImageField(upload_to='media/', null=True)
    stock           = models.IntegerField(null = True)

    def str(self):
        return self.nombre_producto

class TipoProducto(models.Model):
    id_tipo         = models.AutoField(db_column = 'idTipo', primary_key=True)
    nombre_tipo     = models.CharField(max_length=50)

    def str(self):
        return self.nombre_tipo
    

