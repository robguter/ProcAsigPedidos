from django.shortcuts import render

from .models import Clientes, Proveedores, Requerimientos

def rndr_home(request):
    return render(request, "home.htm")

def rndrClientes(request):
    oClie = Clientes.objects.all()
    return render(request, "clientes.htm",{"oClies": oClie})

def rndrProveedores(request):
    oProv = Proveedores.objects.all()
    return render(request, "proveedores.htm",{"oProvs": oProv})

def rndrRequerimientos(request):
    oClie = Clientes.objects.all()
    oProv = Proveedores.objects.all()
    oRequ = Requerimientos.objects.all()
    return render(request, "Requerimientos.htm",{"oRequs": oRequ, "oClies": oClie, "oProvs": oProv})
