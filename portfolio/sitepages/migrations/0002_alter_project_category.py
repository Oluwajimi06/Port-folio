# Generated by Django 5.1.1 on 2024-09-21 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitepages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('front_end', 'Front-End'), ('development', 'Development'), ('ecommerce', 'E-commerce')], max_length=50),
        ),
    ]
