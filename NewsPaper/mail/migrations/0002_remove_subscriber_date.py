# Generated by Django 4.2.2 on 2023-08-01 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='date',
        ),
    ]