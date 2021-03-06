# Generated by Django 2.1.1 on 2018-09-27 12:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_ul', '0007_auto_20180926_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='money',
            name='url',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='money',
            name='picture',
            field=models.ImageField(blank=True, default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='money',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 27, 16, 50, 16, 785156), verbose_name='date start'),
        ),
    ]
