# Generated by Django 2.1.2 on 2018-11-06 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchBarApp', '0021_remove_industry_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='industry',
            name='file',
        ),
        migrations.AddField(
            model_name='industry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
