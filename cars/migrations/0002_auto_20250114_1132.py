# Generated by Django 3.0.7 on 2025-01-14 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='milage',
            field=models.IntegerField(),
        ),
    ]
