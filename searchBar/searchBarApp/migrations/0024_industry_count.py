# Generated by Django 2.1.2 on 2018-11-06 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchBarApp', '0023_auto_20181107_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='industry',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]