# Generated by Django 4.2.1 on 2023-08-04 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metamesh', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='phone_number',
            field=models.CharField(default='', max_length=12),
        ),
    ]