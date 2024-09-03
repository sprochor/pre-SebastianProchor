from django.db import models

class Empleado(models.Model):
    class Estado(models.TextChoices):
        CANDIDATO = 'CANDIDATO', 'Candidato'
        ACTIVO = 'ACTIVO', 'Activo'
        PASIVO = 'PASIVO', 'Pasivo'
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cuil = models.CharField(max_length=11, unique=True)
    direccion = models.CharField(max_length=200)
    activo = models.BooleanField(default=True)
    sueldo = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    estado = models.CharField(max_length=10, choices=Estado.choices, default=Estado.CANDIDATO)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} ({self.cuil}) "

class Empresa(models.Model):
    razon_social = models.CharField(max_length=100)
    cuit = models.CharField(max_length=11, unique=True)
    rubro = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.razon_social} {self.rubro} ({self.cuit}) "

class Liquidacion(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)  
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE) 
    fecha = models.DateField(auto_now_add=True)  
    sueldo_bruto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"Payroll de {self.empleado} en {self.empresa} - {self.fecha}"