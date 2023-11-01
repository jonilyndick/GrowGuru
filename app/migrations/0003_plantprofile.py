# Generated by Django 4.1.7 on 2023-10-13 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_plantspecies_options_plantspecies_common_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=255)),
                ('plant_origin', models.CharField(max_length=255)),
                ('soil_mix', models.CharField(max_length=255)),
                ('last_repot', models.DateField()),
                ('moss_poles', models.BooleanField(default=False)),
                ('progress_photos', models.ImageField(blank=True, null=True, upload_to='plant_photos/')),
                ('misc_notes', models.TextField(blank=True)),
            ],
        ),
    ]