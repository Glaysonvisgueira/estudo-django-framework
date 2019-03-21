# Generated by Django 2.1.3 on 2019-03-20 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0015_auto_20190320_0027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zonas',
            options={'ordering': ['id'], 'verbose_name': 'Zona', 'verbose_name_plural': 'Zonas'},
        ),
        migrations.RemoveField(
            model_name='zonas',
            name='id_zona',
        ),
        migrations.AddField(
            model_name='zonas',
            name='cidade',
            field=models.CharField(default='', max_length=40, verbose_name='Cidade:'),
        ),
        migrations.AddField(
            model_name='zonas',
            name='uf',
            field=models.CharField(default='', max_length=2, verbose_name='UF:'),
        ),
        migrations.AlterField(
            model_name='zonas',
            name='zona',
            field=models.CharField(default='', max_length=10, verbose_name='Zona:'),
        ),
    ]