# Generated by Django 4.0.4 on 2022-05-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='imagem',
            field=models.ImageField(upload_to='projeto_imagens'),
        ),
    ]
