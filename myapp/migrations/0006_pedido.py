# Generated by Django 5.1.1 on 2024-09-30 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_arreglos_diponibilidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('cedula', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=10)),
                ('nombreR', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('muicipio', models.CharField(max_length=20)),
                ('barrio', models.CharField(max_length=30)),
                ('celularR', models.CharField(max_length=10)),
                ('quienEnvia', models.CharField(max_length=30)),
            ],
        ),
    ]
