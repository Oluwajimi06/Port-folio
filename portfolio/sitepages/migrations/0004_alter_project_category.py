# Generated by Django 5.1.1 on 2024-09-21 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitepages', '0003_project_tech_stack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('Front-end', 'Front-End'), ('Development', 'Development'), ('E-commerce', 'E-commerce')], max_length=50),
        ),
    ]
