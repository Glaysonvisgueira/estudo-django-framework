# Generated by Django 2.1.3 on 2019-01-08 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_motorista_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorista',
            name='CPF',
            field=models.CharField(max_length=11, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='motorista',
            name='num_registro',
            field=models.CharField(max_length=11, verbose_name='Número de registro'),
        ),
        migrations.AlterField(
            model_name='motorista',
            name='rg_identidade',
            field=models.CharField(max_length=13, verbose_name='RG'),
        ),
    ]