# Generated by Django 4.1 on 2022-08-12 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_live_tumnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='bay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Standard1', max_length=50)),
                ('title_hero', models.CharField(default='Bay Bondye', max_length=50)),
                ('subtitle_hero', models.TextField(null=True)),
                ('show', models.BooleanField(default=True)),
            ],
        ),
    ]
