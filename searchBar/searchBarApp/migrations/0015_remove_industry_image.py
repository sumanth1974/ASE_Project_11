# Generated by Django 2.1.2 on 2018-11-06 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchBarApp', '0014_auto_20181106_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='industry',
            name='image',
        ),
    ]