from django.contrib import admin
from .models import Usuario, Docente, Material, Prestamo, DetallePrestamo

admin.site.register(Usuario)
admin.site.register(Docente)
admin.site.register(Material)
admin.site.register(Prestamo)
admin.site.register(DetallePrestamo)
