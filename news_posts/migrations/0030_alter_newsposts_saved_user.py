# Generated by Django 3.2.8 on 2022-02-01 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20220201_1829'),
        ('news_posts', '0029_newsposts_saved_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsposts',
            name='saved_user',
            field=models.ManyToManyField(related_name='saved_user', through='users.bookmarked_posts', to='users.User'),
        ),
    ]