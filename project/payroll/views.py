from django.shortcuts import render, redirect
from .models import Empleado, Empresa, Liquidacion
from .forms import EmpleadoForm, EmpresaForm, LiquidacionForm

def index(request):
    return render(request, "payroll/index.html")

def empleado_list(request):
    query = Empleado.objects.all
    context = {"object_list": query}
    return render(request, "payroll/empleado_list.html", context)

def empresa_list(request):
    query = Empresa.objects.all
    context = {"object_list": query}
    return render(request, "payroll/empresa_list.html", context)

def liquidacion_list(request):
    query = Liquidacion.objects.all
    context = {"object_list": query}
    return render(request, "payroll/liquidacion_list.html", context)

def empleado_create(request):
    if request.method == "GET":
        form = EmpleadoForm()
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("empleado_list")
    return render(request, "payroll/empleado_create.html", {"form": form})

def empresa_create(request):
    if request.method == "GET":
        form = EmpresaForm()
    if request.method == "POST":
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("empresa_list")
    return render(request, "payroll/empresa_create.html", {"form": form})

def liquidacion_create(request):
    if request.method == "GET":
        form = LiquidacionForm()
    if request.method == "POST":
        form = LiquidacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("empresa_list")
    return render(request, "payroll/liquidacion_create.html", {"form": form})