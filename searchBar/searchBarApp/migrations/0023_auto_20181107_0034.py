# Generated by Django 2.1.2 on 2018-11-06 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchBarApp', '0022_auto_20181106_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='industry',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='industry',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
