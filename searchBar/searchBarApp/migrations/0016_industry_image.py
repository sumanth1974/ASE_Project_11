# Generated by Django 2.1.2 on 2018-11-06 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchBarApp', '0015_remove_industry_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='industry',
            name='image',
            field=models.CharField(default='', max_length=264),
        ),
    ]
