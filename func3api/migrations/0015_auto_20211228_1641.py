# Generated by Django 3.2.8 on 2021-12-28 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('func3api', '0014_auto_20211228_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpu',
            name='Vendor',
        ),
        migrations.RemoveField(
            model_name='display',
            name='Vendor',
        ),
        migrations.RemoveField(
            model_name='ssd',
            name='Vendor',
        ),
    ]