from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROL_CHOICES = (
        ('ADMIN', 'Administrador'),
        ('PANOL', 'Pañol'),
    )
    rol = models.CharField(max_length=10, choices=ROL_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"

class Docente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.rut})"

class Material(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Prestamo(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.PROTECT)
    panol = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        limit_choices_to={'rol': 'PANOL'},
        related_name='prestamos_realizados'
    )
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Préstamo a {self.docente} el {self.fecha.strftime('%Y-%m-%d')}"

class DetallePrestamo(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE, related_name='detalles')
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.material.nombre}"
