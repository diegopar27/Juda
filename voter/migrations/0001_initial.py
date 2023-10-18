# Generated by Django 4.2 on 2023-10-18 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('lastname', models.CharField(max_length=100, verbose_name='Apellido')),
                ('type_of_document', models.CharField(choices=[('cedula', 'Cedula'), ('tarjeta de identidad', 'Tarjeta de identidad'), ('cedula extrangera', 'Cedula extrenagera')], max_length=100, verbose_name='Tipo de documento')),
                ('document_number', models.CharField(max_length=100, verbose_name='Numero de documento')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electronico')),
                ('address_of_residence', models.CharField(max_length=100, verbose_name='Direccion de residencia')),
                ('phone', models.CharField(max_length=100, verbose_name='Celular')),
            ],
        ),
    ]
