# Generated by Django 5.0.6 on 2024-05-29 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='types',
            field=models.CharField(blank=True, choices=[('IT', 'IT'), ('NON IT', 'Non IT'), ('mobile phones', 'Mobile Phones')], max_length=100, null=True),
        ),
    ]
