# Generated by Django 2.1.2 on 2018-11-03 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchBarApp', '0007_auto_20181104_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industry',
            name='date',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]
