# Generated by Django 4.2.4 on 2023-09-05 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moda', '0003_conteudosegundomain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='path',
            field=models.ImageField(upload_to='images/site'),
        ),
    ]
