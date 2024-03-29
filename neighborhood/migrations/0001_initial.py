# Generated by Django 4.2 on 2023-11-10 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('commune', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_neighborhood', models.CharField(max_length=50, verbose_name='Nombre del barrio')),
                ('n_commune', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commune.commune', verbose_name='nombre de la comuna')),
            ],
        ),
    ]
