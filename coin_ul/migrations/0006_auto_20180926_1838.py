# Generated by Django 2.1.1 on 2018-09-26 14:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_ul', '0005_auto_20180923_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 26, 18, 38, 29, 355468), verbose_name='date start'),
        ),
    ]