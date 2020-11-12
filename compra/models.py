from django.db import models

# Create your models here.

# TABLA MATERIA PRIMA
class MateriaPrima( models.Model):
    descripcion = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    
    def __str__(self):
        return self.descripcion

# TABLA  PROVEEDOR
class Proveedor( models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30)
    email = models.EmailField
        # aca la relacion
    compras = models.ManyToManyField(MateriaPrima, through='Compra')    
    def __str__(self):
        return self.nombre



# TABLA INTERMEDIA ENTRE (MATERIA PRIMA CON PROVEEDOR) //RELACION MUCHOS A MUCHOS
class Compra (models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    materiaprima = models.ForeignKey(MateriaPrima, on_delete=models.CASCADE)
    date_joined = models.DateField()

    def __str__(self):
        return self.proveedor

