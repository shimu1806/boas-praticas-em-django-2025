# Generated by Django 5.1.5 on 2025-03-27 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnCastellinaEv1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='imagem',
            field=models.ImageField(blank=True, help_text='Imagem representativa do local.', null=True, upload_to='static/learnCasttelinaEv1/src/', verbose_name='Imagem'),
        ),
    ]
