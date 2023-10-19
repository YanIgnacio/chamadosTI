# Generated by Django 4.2.5 on 2023-10-17 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chamadosApp', '0004_endereco_secretaria_chamado_descricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servidor',
            name='secretaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chamadosApp.secretaria', verbose_name='Secretaria'),
        ),
        migrations.AlterField(
            model_name='servidor',
            name='setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chamadosApp.setor', verbose_name='Setor'),
        ),
    ]