from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero    = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)

class Alumno(models.Model):
    rut                 = models.CharField(primary_key=True, max_length=10)
    nombre              = models.CharField(max_length=20)
    apellido_paterno    = models.CharField(max_length=20)
    apellido_materno    = models.CharField(max_length=20)
    fecha_nacimiento    = models.DateField(blank=False, null=False)
    id_genero           = models.ForeignKey('Genero',on_delete=models.CASCADE,db_column='idGenero')
    telefono            = models.CharField(max_length=45)
    email               = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion           = models.CharField(max_length=50, blank=True, null=False)
    activo              = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)

# -------------------
# NUEVOS MODELOS
# -------------------
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre      = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio      = models.DecimalField(max_digits=10, decimal_places=2)
    stock       = models.IntegerField(default=0)
    imagen      = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Wishlist(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    agregado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'producto')

    def __str__(self):
        return f"{self.usuario.username} - {self.producto.nombre}"
