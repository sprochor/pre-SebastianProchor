from django import forms
from .models import Empleado, Empresa, Liquidacion

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = "__all__"  # Correcto

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = "__all__"  # Correcto

class LiquidacionForm(forms.ModelForm):
    empleado = forms.ModelChoiceField(
        queryset=Empleado.objects.all(), empty_label="Selecione un empleado"
    )
    empresa = forms.ModelChoiceField(
        
        queryset=Empresa.objects.all(), empty_label="Selecione una empresa"
    )
    class Meta:
        model = Liquidacion
        fields = "__all__"