# Generated by Django 4.0.2 on 2022-03-04 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='descricao',
            field=models.TextField(max_length=150, verbose_name='Descricao'),
        ),
    ]
