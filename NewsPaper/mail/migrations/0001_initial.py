# Generated by Django 4.2.2 on 2023-07-28 22:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date', models.DateField(default=datetime.datetime.utcnow)),
                ('subscribed_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
