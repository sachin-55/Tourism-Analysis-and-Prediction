# Generated by Django 2.0.7 on 2019-08-06 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SearchEngine', '0002_auto_20190805_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='viewname',
            field=models.TextField(default='index', max_length=1000),
        ),
    ]
