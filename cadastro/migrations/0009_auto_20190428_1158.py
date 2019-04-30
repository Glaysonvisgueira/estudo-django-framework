# Generated by Django 2.1.3 on 2019-04-28 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0008_auto_20190428_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorista',
            name='data_expedicao_rg',
            field=models.DateField(verbose_name='Data de expedição do RG:'),
        ),
        migrations.AlterField(
            model_name='motorista',
            name='emissao_cnh',
            field=models.DateField(verbose_name='Data de emissão da CNH:'),
        ),
        migrations.AlterField(
            model_name='motorista',
            name='nascimento',
            field=models.DateField(verbose_name='Data de nascimento:'),
        ),
        migrations.AlterField(
            model_name='motorista',
            name='validade_habilitacao',
            field=models.DateField(verbose_name='Validade da habilitação:'),
        ),
    ]