# Generated by Django 3.1 on 2023-01-19 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_product_discount_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_percentage',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]