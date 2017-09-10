# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Empresa(models.Model):
	usuario=models.CharField(max_length=15)
	contrasenia=models.CharField(max_length=20)
	nombreEmpresa=models.CharField(max_length=30)
	email=models.EmailField(max_length=50)
	telefono=models.CharField(max_length=8)
	ubicacion=models.CharField(max_length=150)
	rubro=models.CharField(max_length=25)

	class Meta:
		verbose_name='Empresa'
		verbose_name_plural='Empresas'
	def __str__(self):
		return '%s' %(self.nombreEmpresa)

class Facultad(models.Model):
	nombreFacultad=models.CharField(max_length=35)

	class Meta:
		verbose_name='Facultad'
		verbose_name_plural='Facultades'
	def __str__(self):
		return '%s' %(self.nombreFacultad)

class Carrera(models.Model):
	facultad=models.ForeignKey(Facultad)
	nombreCarrera=models.CharField(max_length=35)

	class Meta:
		verbose_name='Carrera'
		verbose_name_plural='Carreras'
	def __str__(self):
		return '%s' %(self.nombreCarrera)

class OfertaEmpleo(models.Model):
	empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE)
	nombre=models.CharField(max_length=50)
	#area=models.CharField(max_length=50)
	puestos=models.IntegerField()
	tipoContrato=models.CharField(max_length=50)
	nivelExperiencia=models.CharField(max_length=25)
	genero=models.CharField(max_length=15)
	edadMin=models.IntegerField()
	edadMax=models.IntegerField()
	salarioMax=models.IntegerField()
	salarioMim=models.IntegerField()
	departamento=models.CharField(max_length=50)