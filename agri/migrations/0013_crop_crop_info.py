# Generated by Django 4.0 on 2021-12-18 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0012_alter_crop_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='crop_info',
            field=models.CharField(default=10, max_length=3000),
        ),
    ]
