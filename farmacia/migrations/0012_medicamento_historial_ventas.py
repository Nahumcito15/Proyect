# Generated by Django 4.2.7 on 2023-12-07 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0011_alter_venta_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='historial_ventas',
            field=models.ManyToManyField(related_name='medicamentos_vendidos', through='farmacia.DetalleVenta', to='farmacia.venta'),
        ),
    ]
