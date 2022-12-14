# Generated by Django 3.2.16 on 2022-10-14 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('variedade', models.CharField(max_length=200)),
                ('qualidade', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Produtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('endereco', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=200)),
            ],
        ),
    ]
