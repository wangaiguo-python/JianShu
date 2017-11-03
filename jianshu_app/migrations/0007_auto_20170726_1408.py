# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jianshu_app', '0006_article_btime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Btime',
            field=models.DateTimeField(verbose_name='创建时间', auto_now_add=True),
        ),
    ]
