# Generated by Django 5.1.1 on 2024-10-22 02:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_remove_pedido_arreglo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='arreglo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.arreglos'),
            preserve_default=False,
        ),
    ]
