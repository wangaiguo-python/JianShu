# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jianshu_app', '0001_createsuperuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='名称', max_length=128)),
                ('content', models.TextField(verbose_name='内容')),
                ('views', models.IntegerField(verbose_name='阅读量', default=0)),
                ('likes', models.IntegerField(verbose_name='喜欢数', default=0)),
                ('comments', models.IntegerField(verbose_name='评论数', default=0)),
                ('cover', models.ImageField(verbose_name='封面', upload_to='')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='名称', max_length=20)),
                ('img', models.ImageField(verbose_name='封面', upload_to='')),
                ('Btime', models.DateTimeField(verbose_name='创建时间', default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': '专题',
                'verbose_name_plural': '专题',
            },
        ),
        migrations.AddField(
            model_name='testarticle',
            name='topic',
            field=models.ForeignKey(verbose_name='专题', related_name='articles', to='jianshu_app.Topic'),
        ),
    ]
