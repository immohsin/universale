# Generated by Django 2.0.2 on 2018-07-23 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ffs', '0010_auto_20180720_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='flag_count',
            field=models.IntegerField(default=0),
        ),
    ]
