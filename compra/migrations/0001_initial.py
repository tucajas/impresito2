# Generated by Django 3.1.1 on 2020-11-12 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MateriaPrima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('stock', models.IntegerField(default=0)),
                ('precio', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=30)),
                ('compras', models.ManyToManyField(through='compra.Compra', to='compra.MateriaPrima')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='materiaprima',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compra.materiaprima'),
        ),
        migrations.AddField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compra.proveedor'),
        ),
    ]
