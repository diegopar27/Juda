# Generated by Django 4.2 on 2023-10-18 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leader', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_neighborhood', models.CharField(max_length=50, verbose_name='Nombre del barrio')),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood_leader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaders', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leader.leader', verbose_name='Lider')),
                ('neighborhoods', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='neighborhood.neighborhood', verbose_name='user')),
            ],
        ),
    ]
