# Generated by Django 4.2.2 on 2023-08-22 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_alter_post_options_alter_category_subscribers'),
        ('users', '0003_rename_user_subscriber_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.category', verbose_name='Категории'),
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]
