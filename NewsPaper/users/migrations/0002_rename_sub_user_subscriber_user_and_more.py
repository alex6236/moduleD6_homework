# Generated by Django 4.2.2 on 2023-08-16 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_alter_post_options_alter_category_subscribers'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='sub_user',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='sub_email',
        ),
        migrations.AddField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Почта'),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='news.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
