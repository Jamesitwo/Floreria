# Generated by Django 5.1.1 on 2024-10-26 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_pedido_arreglo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='categorias',
            new_name='Categoria',
        ),
        migrations.RenameModel(
            old_name='compras_tienda',
            new_name='Compra_tienda',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='arreglo',
        ),
        migrations.RenameModel(
            old_name='arreglos',
            new_name='Arreglo',
        ),
        migrations.CreateModel(
            name='PedidoArreglo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('arreglo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.arreglo')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedido_arreglos', to='myapp.pedido')),
            ],
        ),
    ]
