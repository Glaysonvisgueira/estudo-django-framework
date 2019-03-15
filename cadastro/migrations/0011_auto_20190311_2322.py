# Generated by Django 2.1.3 on 2019-03-12 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0010_auto_20190311_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontosDeVisitas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=120, verbose_name='Cliente:')),
                ('cpf', models.CharField(max_length=120, verbose_name='CPF:')),
                ('endereco', models.CharField(max_length=120, verbose_name='Endereço:')),
                ('complemento', models.CharField(blank=True, max_length=120, verbose_name='Complemento:')),
                ('bairro', models.CharField(max_length=40, verbose_name='Bairro:')),
                ('cep', models.CharField(max_length=8, verbose_name='CEP:')),
                ('cidade', models.CharField(max_length=30, verbose_name='Cidade:')),
                ('uf', models.CharField(default='BR', max_length=2, verbose_name='UF:')),
            ],
            options={
                'verbose_name': 'Ponto de visita',
                'verbose_name_plural': 'Pontos de visitas',
                'ordering': ['bairro'],
            },
        ),
        migrations.DeleteModel(
            name='PontosDeVisita',
        ),
    ]
