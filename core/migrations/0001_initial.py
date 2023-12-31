# Generated by Django 4.2.5 on 2023-11-24 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gremio',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre_Gremio', models.CharField(max_length=150)),
                ('RUC_Gremio', models.CharField(max_length=11)),
                ('DNI_Secretario_General', models.CharField(max_length=8)),
                ('Nombre_Secretario_General', models.CharField(max_length=150)),
                ('DNI_Dirigente', models.CharField(max_length=8)),
                ('Nombre_Dirigente', models.CharField(max_length=150)),
                ('DNI_Presidente', models.CharField(max_length=8)),
                ('Nombre_Presidente', models.CharField(max_length=150)),
                ('Foto_Gremio', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('DNI', models.CharField(max_length=50)),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Fecha_Nacimiento', models.DateField()),
                ('Departamento', models.CharField(max_length=50)),
                ('Provincia', models.CharField(max_length=50)),
                ('Distrito', models.CharField(max_length=50)),
                ('Sexo', models.CharField(max_length=10)),
                ('Domicilio', models.CharField(max_length=200)),
                ('Nombre_Padre', models.CharField(max_length=100)),
                ('Nombre_Madre', models.CharField(max_length=100)),
                ('Foto_Persona', models.CharField(max_length=200)),
            ],
        ),
    ]
