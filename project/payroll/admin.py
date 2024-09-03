from django.contrib import admin
from .models import Empleado, Empresa, Liquidacion

admin.site.register(Empleado)
admin.site.register(Empresa)
admin.site.register(Liquidacion)