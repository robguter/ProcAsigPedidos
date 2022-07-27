from django.contrib import admin

from AppRequerimientos.models import Clientes, Proveedores, Requerimientos

class ClientesAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class ProveedoresAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class RequerimientosAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Proveedores, ProveedoresAdmin)
admin.site.register(Requerimientos, RequerimientosAdmin)