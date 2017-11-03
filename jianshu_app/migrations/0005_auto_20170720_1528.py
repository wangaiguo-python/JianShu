# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jianshu_app', '0004_auto_20170720_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='名称', max_length=128)),
                ('cover', models.ImageField(verbose_name='封面', upload_to='')),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='内容 ', blank=True)),
                ('views', models.IntegerField(verbose_name='阅读量', default=0)),
                ('likes', models.IntegerField(verbose_name='喜欢数', default=0)),
                ('comments', models.IntegerField(verbose_name='评论数', default=0)),
                ('topic', models.ForeignKey(verbose_name='专题', related_name='articles', to='jianshu_app.Topic')),
                ('user', models.ForeignKey(verbose_name='用户', related_name='articles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.RemoveField(
            model_name='testarticle',
            name='topic',
        ),
        migrations.DeleteModel(
            name='UArticle',
        ),
        migrations.DeleteModel(
            name='TestArticle',
        ),
    ]
