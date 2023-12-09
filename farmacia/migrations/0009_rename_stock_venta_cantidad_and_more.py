# Generated by Django 4.2.7 on 2023-11-20 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0008_medicamento_fecha_ingreso_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='stock',
            new_name='cantidad',
        ),
        migrations.AlterField(
            model_name='medicamento',
            name='fecha_ingreso',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='medicamento',
            name='fecha_vencimiento',
            field=models.DateField(),
        ),
    ]