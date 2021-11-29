# Generated by Django 3.2.8 on 2021-11-26 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_username'),
        ('communities', '0003_communities_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communities',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin', to='users.user'),
        ),
        migrations.AlterField(
            model_name='communities',
            name='is_nsfw',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]