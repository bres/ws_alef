# Generated by Django 3.1 on 2023-02-15 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_heroimages_herotitle_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroimages',
            name='hero_subtitle',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='heroimages',
            name='hero_title',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]