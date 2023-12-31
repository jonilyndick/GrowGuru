# Generated by Django 4.1.7 on 2023-10-09 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plantspecies',
            options={'verbose_name': 'Plant Species', 'verbose_name_plural': 'Plant Species'},
        ),
        migrations.AddField(
            model_name='plantspecies',
            name='common_name',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='plantspecies',
            name='name',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
