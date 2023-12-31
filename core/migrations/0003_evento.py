# Generated by Django 4.2.5 on 2023-11-25 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_persona_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('opcion', models.CharField(max_length=255)),
                ('departamento', models.CharField(max_length=255)),
                ('provincia', models.CharField(max_length=255)),
                ('distrito', models.CharField(max_length=255)),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('nombreGremio', models.CharField(max_length=255)),
                ('medida', models.CharField(max_length=255)),
                ('resumenSummary', models.TextField()),
            ],
        ),
    ]
