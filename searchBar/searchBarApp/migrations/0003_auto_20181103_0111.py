# Generated by Django 2.1.2 on 2018-11-02 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchBarApp', '0002_industry_website_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industry',
            name='website_url',
            field=models.CharField(max_length=264, unique=True),
        ),
    ]