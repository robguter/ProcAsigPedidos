from django.urls import path

from AppRequerimientos.views import rndrClientes, rndrProveedores, rndrRequerimientos

urlpatterns = [
    path('clientes/', rndrClientes, name='Clientes'),
    path('proveedores/', rndrProveedores, name='Proveedores'),
    path('', rndrRequerimientos, name='Requerimientos'),
]