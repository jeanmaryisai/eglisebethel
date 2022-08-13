# Generated by Django 4.1 on 2022-08-12 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_img_evenement_estimatedduration_evenement_show_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='evenement',
            name='cover',
            field=models.ImageField(null=True, upload_to='media/images/%y'),
        ),
        migrations.AddField(
            model_name='img',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='evenement',
            name='album',
            field=models.ManyToManyField(blank=True, null=True, to='home.img'),
        ),
        migrations.AlterField(
            model_name='evenement',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
