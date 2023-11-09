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