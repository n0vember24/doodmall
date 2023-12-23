# Generated by Django 5.0 on 2023-12-23 11:08

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Title of Category')),
                ('about', models.TextField(blank=True, help_text='Not required. The description must consist minimum 25 and maximum 250 characters.', max_length=250, null=True)),
                ('slug', models.SlugField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Name of Country')),
                ('slug', models.SlugField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Title of Product')),
                ('slug', models.SlugField(max_length=200, validators=[django.core.validators.MinLengthValidator(5)])),
                ('is_exists', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('count', models.PositiveSmallIntegerField(default=1, verbose_name='Count of products')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Title of Subcategory')),
                ('slug', models.SlugField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Required. The title must consist minimum 2 and maximum 30 characters.', max_length=30, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Title of brand')),
                ('about', models.TextField(blank=True, help_text='Not required. The description must consist minimum 50 and maximum 500 characters.', max_length=500, null=True, verbose_name='Description of the brand')),
                ('logo', models.ImageField(upload_to='brands/logos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))], verbose_name='Logo of the brand')),
                ('found_year', models.DateField(blank=True, null=True, verbose_name='Year of brand foundation')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.country')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
