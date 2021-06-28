# Generated by Django 3.2.4 on 2021-06-24 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=100)),
                ('price', models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ('image_link', models.CharField(blank=True, max_length=50, null=True)),
                ('brand', models.CharField(blank=True, max_length=150, null=True)),
                ('category', models.CharField(blank=True, max_length=150, null=True)),
                ('product_type', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.CharField(blank=True, max_length=1500, null=True)),
            ],
        ),
    ]