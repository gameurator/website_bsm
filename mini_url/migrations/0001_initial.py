# Generated by Django 2.1.2 on 2018-11-03 21:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiniURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100, unique=True, verbose_name='url')),
                ('code', models.CharField(max_length=6, unique=True, verbose_name='code')),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2018, 11, 3, 21, 13, 56, 135701, tzinfo=utc), verbose_name='creation date')),
                ('pseudo', models.CharField(max_length=255, verbose_name='pseudo')),
                ('count_access', models.IntegerField(default=0, verbose_name='access counter')),
            ],
            options={
                'verbose_name': 'mini_URL',
                'ordering': ['creation_date'],
            },
        ),
    ]
