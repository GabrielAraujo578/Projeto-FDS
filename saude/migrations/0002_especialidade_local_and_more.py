# Generated by Django 5.1.1 on 2024-09-30 14:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saude', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='historicomedico',
            name='doencas_preexistentes',
        ),
        migrations.RemoveField(
            model_name='historicomedico',
            name='genero',
        ),
        migrations.RemoveField(
            model_name='historicomedico',
            name='medicamentos_atual',
        ),
        migrations.RemoveField(
            model_name='historicomedico',
            name='nome_paciente',
        ),
        migrations.AddField(
            model_name='historicomedico',
            name='doencas',
            field=models.TextField(blank=True, default='Sem deonças pré-existentes'),
        ),
        migrations.AddField(
            model_name='historicomedico',
            name='medicacao',
            field=models.TextField(blank=True, default='Não usa medicamento'),
        ),
        migrations.AddField(
            model_name='historicomedico',
            name='nome',
            field=models.CharField(default='Sem nome', max_length=100),
        ),
        migrations.AlterField(
            model_name='historicomedico',
            name='alergias',
            field=models.TextField(blank=True, default='Sem alergias'),
        ),
        migrations.AlterField(
            model_name='historicomedico',
            name='cirugias',
            field=models.TextField(blank=True, default='Sem cirugias'),
        ),
        migrations.AlterField(
            model_name='historicomedico',
            name='idade',
            field=models.PositiveIntegerField(default=0),
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
