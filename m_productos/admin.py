from django.contrib import admin
from .models import ModeloProducto, Detalle_boleta, Boleta

# Register your models here.

admin.site.register(ModeloProducto)
admin.site.register(Detalle_boleta)
admin.site.register(Boleta)