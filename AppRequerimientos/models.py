from django.db import models
from django.db.models import BigAutoField, CharField, EmailField, IntegerChoices
from django.forms import IntegerField
from django.utils.translation import gettext_lazy as _

class Clientes(models.Model):
    idcte = BigAutoField(
        auto_created=True, primary_key=True, null=False, serialize=False, verbose_name='ID')
    cedrif = CharField(max_length=75, null=False, verbose_name='Cedula o Rif')
    nombre = CharField(max_length=75, null=False, verbose_name='Nombre')
    direccion = CharField(max_length=75, null=False, verbose_name='Dirección')
    telefono = CharField(max_length=75, null=False, verbose_name='Teléfono')
    correo = EmailField(blank=False, null=False, verbose_name='Correo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Actualizado')
    
    class Meta:
        db_table = "clientes"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    def __str__(self):
            return self.cedrif

class Proveedores(models.Model):
    idprov = BigAutoField(
        auto_created=True, primary_key=True, null=False, serialize=False, verbose_name='ID')
    cedrif = CharField(max_length=75, null=False, verbose_name='Cedula o Rif')
    nombre = CharField(max_length=75, null=False, verbose_name='Nombre')
    direccion = CharField(max_length=75, null=False, verbose_name='Dirección')
    telefono = CharField(max_length=75, null=False, verbose_name='Teléfono')
    correo = EmailField(blank=False, null=False, verbose_name='Correo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Actualizado')
    
    class Meta:
        db_table = "proveedores"
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
    def __str__(self):
            return self.cedrif

class Tipo(models.IntegerChoices):
        FOTO = 1
        VIDEO = 2
        PLANO = 3

class Requerimientos(models.Model):
    idreq = BigAutoField(auto_created=True, primary_key=True, null=False, serialize=False, verbose_name='ID')
    nombre = CharField(max_length=75, null=False, verbose_name='Nombre')
    tipo = models.IntegerField(choices=Tipo.choices, default=Tipo.FOTO, null=False, verbose_name='Tipo')
    idcte = models.ForeignKey(Clientes, on_delete=models.CASCADE, verbose_name='ID Cliente')
    idprov = models.ForeignKey(Proveedores, on_delete=models.CASCADE, verbose_name='ID Proveedor')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Actualizado')
    
    class Meta:
        db_table = "requerimientos"
        verbose_name = "Requerimiento"
        verbose_name_plural = "Requerimientos"
    def __str__(self):
            return self.nombre
