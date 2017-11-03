# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('jianshu_app', '0002_auto_20170720_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='UArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Content', DjangoUeditor.models.UEditorField(verbose_name='内容 ', blank=True)),
            ],
            options={
                'verbose_name': '富文本编辑',
                'verbose_name_plural': '富文本编辑',
            },
        ),
    ]
