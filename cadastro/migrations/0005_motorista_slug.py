# Generated by Django 2.1.3 on 2019-01-08 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_auto_20190108_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='motorista',
            name='slug',
            field=models.SlugField(default='', verbose_name='Código do motorista'),
            preserve_default=False,
        ),
    ]
