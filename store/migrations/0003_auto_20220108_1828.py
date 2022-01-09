# Generated by Django 3.1 on 2022-01-08 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20220108_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='strap',
        ),
        migrations.AddField(
            model_name='product',
            name='max_strap',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='min_strap',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]
