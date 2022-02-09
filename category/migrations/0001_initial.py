# Generated by Django 3.1 on 2022-02-09 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('cat_image', models.ImageField(upload_to='images/categories')),
                ('sort_number', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='HeroImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_title', models.TextField(max_length=200)),
                ('hero_link', models.CharField(blank=True, max_length=200)),
                ('hero_image', models.ImageField(upload_to='images/heros')),
                ('hero_number', models.CharField(max_length=50, unique=True)),
                ('hero_href', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name': 'hero_image',
                'verbose_name_plural': 'hero_images',
            },
        ),
    ]
