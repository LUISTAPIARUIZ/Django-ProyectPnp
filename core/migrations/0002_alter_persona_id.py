# Generated by Django 4.2.5 on 2023-11-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
