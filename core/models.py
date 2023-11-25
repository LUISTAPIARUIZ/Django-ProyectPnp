from django.db import models

# Create your models here.

class Gremio(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre_Gremio = models.CharField(max_length=150)
    RUC_Gremio = models.CharField(max_length=11)
    DNI_Secretario_General = models.CharField(max_length=8)
    Nombre_Secretario_General = models.CharField(max_length=150)
    DNI_Dirigente = models.CharField(max_length=8)
    Nombre_Dirigente = models.CharField(max_length=150)
    DNI_Presidente = models.CharField(max_length=8)
    Nombre_Presidente = models.CharField(max_length=150)
    Foto_Gremio = models.CharField(max_length=200)

class Persona(models.Model):
    id=models.AutoField(primary_key=True)
    DNI = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Fecha_Nacimiento = models.DateField()
    Departamento = models.CharField(max_length=50)
    Provincia = models.CharField(max_length=50)
    Distrito = models.CharField(max_length=50)
    Sexo = models.CharField(max_length=10)
    Domicilio = models.CharField(max_length=200)
    Nombre_Padre = models.CharField(max_length=100)
    Nombre_Madre = models.CharField(max_length=100)
    Foto_Persona = models.CharField(max_length=200)


class Evento(models.Model):
    id=models.AutoField(primary_key=True)
    opcion = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    distrito = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    nombreGremio = models.CharField(max_length=255)
    medida = models.CharField(max_length=255)
    resumenSummary = models.TextField()