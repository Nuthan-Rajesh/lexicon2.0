# Generated by Django 4.0 on 2021-12-18 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0017_crop_climate_crop_soil_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='climate',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='crop',
            name='soil_info',
            field=models.TextField(max_length=1000),
        ),
    ]
