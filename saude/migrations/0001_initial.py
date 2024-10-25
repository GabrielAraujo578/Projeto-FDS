# Generated by Django 5.1.1 on 2024-10-24 14:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bairros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricoMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='Sem nome', max_length=100)),
                ('idade', models.PositiveIntegerField(default=0)),
                ('medicacao', models.TextField(blank=True, default='Não usa medicamento', null=True)),
                ('doencas', models.TextField(blank=True, default='Sem doenças pré-existentes', null=True)),
                ('cirugias', models.TextField(blank=True, default='Sem cirurgias', null=True)),
                ('alergias', models.TextField(blank=True, default='Sem alergias', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Locais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('bairro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saude.bairros')),
            ],
        ),
        migrations.CreateModel(
            name='Info_local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(blank=True, null=True)),
                ('locais', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='saude.locais')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('especialista', models.CharField(max_length=100)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('especialidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saude.especialidade')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saude.local')),
            ],
        ),
        migrations.CreateModel(
            name='SintomasUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sintomas', models.TextField()),
                ('periodo', models.CharField(default='Desconhecido', max_length=100)),
                ('dor', models.IntegerField(default=0)),
                ('quando_dor', models.CharField(default='Nunca', max_length=50)),
                ('algo_mais', models.TextField(blank=True, default='N/A')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
