# Generated by Django 2.2.13 on 2020-08-27 19:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('estagio', '0003_documentoestagiomodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='conveniomodel',
            name='data_validade',
            field=models.DateTimeField(default=datetime.datetime(2025, 8, 27, 19, 11, 25, 722449, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='conveniomodel',
            name='validade',
            field=models.CharField(choices=[('1', '06 meses'), ('2', '1 ano'), ('3', '2 anos'), ('4', '3 anos'), ('5', '4 anos'), ('6', '5 anos')], default='6', max_length=2, verbose_name='Validade Convênio'),
        ),
        migrations.AlterField(
            model_name='documentoestagiomodel',
            name='curso_fatec',
            field=models.CharField(choices=[('0', 'Sistemas para Internet'), ('1', 'Gestão Empresarial')], default='1', max_length=2, verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='documentoestagiomodel',
            name='tipo_documento',
            field=models.CharField(choices=[('0', 'Termo de compromisso de Estágio'), ('1', 'Plano de Atividades'), ('2', 'Termo Aditivo'), ('3', 'Rescisão de Contrato'), ('4', 'Ficha de avaliação do estagiário'), ('5', 'Relatório Parcial de Estágio'), ('6', 'Relatório Final de Estágio')], default='1', max_length=2, verbose_name='Tipo de Documento'),
        ),
    ]