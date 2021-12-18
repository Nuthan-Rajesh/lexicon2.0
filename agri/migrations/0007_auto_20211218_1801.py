# Generated by Django 3.2.5 on 2021-12-18 12:31

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0006_auto_20211218_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, region=None)),
                ('is_farmer', models.BooleanField(default=False)),
                ('is_Employee', models.BooleanField(default=False)),
                ('is_private', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='govempuser',
            name='Email',
        ),
    ]
