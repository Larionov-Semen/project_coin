# Generated by Django 2.1.1 on 2018-09-26 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_ul', '0006_auto_20180926_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='email',
            field=models.EmailField(default='none', max_length=254),
        ),
        migrations.AlterField(
            model_name='money',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 26, 18, 39, 2, 621093), verbose_name='date start'),
        ),
    ]
