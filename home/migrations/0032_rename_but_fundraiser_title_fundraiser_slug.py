# Generated by Django 4.1 on 2022-08-19 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_fundraiser_endlessfund'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fundraiser',
            old_name='But',
            new_name='title',
        ),
        migrations.AddField(
            model_name='fundraiser',
            name='slug',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
