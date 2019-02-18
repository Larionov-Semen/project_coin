# Generated by Django 2.1.1 on 2018-09-10 05:55

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('choice_sum', models.FloatField(default=0)),
                ('num', models.IntegerField(default=0)),
                ('time', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('year', models.IntegerField(default=2000)),
                ('description', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2018, 9, 10, 9, 55, 27, 668078), verbose_name='date start')),
                ('status', models.CharField(choices=[('ЕСТЬ', 'есть в наличие'), ('НЕТ', 'нет в наличие'), ('ОТМЕНА', 'отменён')], default='Открыт', max_length=7)),
                ('num', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='lot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_1', to='coin_ul.Money'),
        ),
    ]