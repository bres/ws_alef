# Generated by Django 3.1 on 2022-01-16 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='min_max',
            new_name='length_strap',
        ),
        migrations.AddField(
            model_name='product',
            name='care',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
