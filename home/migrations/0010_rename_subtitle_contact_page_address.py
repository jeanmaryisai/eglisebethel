# Generated by Django 4.1 on 2022-08-11 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_contact_page_subtitle_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_page',
            old_name='subtitle',
            new_name='address',
        ),
    ]
