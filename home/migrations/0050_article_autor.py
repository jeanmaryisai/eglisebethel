# Generated by Django 4.1 on 2023-03-24 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0049_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='autor',
            field=models.CharField(default='my self', max_length=100),
            preserve_default=False,
        ),
    ]
