# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jianshu_app', '0005_auto_20170720_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Btime',
            field=models.DateTimeField(verbose_name='创建时间', default=datetime.datetime(2017, 7, 26, 5, 50, 6, 893604, tzinfo=utc), auto_created=True),
            preserve_default=False,
        ),
    ]
