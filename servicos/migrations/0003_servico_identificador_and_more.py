# Generated by Django 5.0 on 2024-09-12 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0002_alter_servico_protocolo'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='identificador',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='categoriamanutencao',
            name='titulo',
            field=models.CharField(choices=[('TVM', 'Trocar válvula do  moto'), ('TO', 'Troca de oleo'), ('B', 'Balanceamento'), ('LNV', 'Lavagem na valeta'), ('LS', 'Lavagem simples'), ('LD', 'Lavagem detalhada'), ('HS', 'Higienizacao simples'), ('HC', 'Higienizacao completa'), ('RP', 'Renovacao de pintura'), ('RC', 'Revisao')], max_length=3),
        ),
    ]
