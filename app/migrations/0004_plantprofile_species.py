# Generated by Django 4.1.7 on 2023-10-13 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_plantprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantprofile',
            name='species',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.plantspecies'),
        ),
    ]
