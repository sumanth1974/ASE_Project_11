# Generated by Django 2.1.2 on 2018-11-06 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchBarApp', '0016_industry_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='industry',
            name='image',
        ),
    ]
