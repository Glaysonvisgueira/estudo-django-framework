# Generated by Django 2.1.3 on 2019-01-06 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_auto_20190106_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='about',
            field=models.TextField(blank=True, verbose_name='Sobre o curso'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descrição simples'),
        ),
    ]