# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-02 06:22
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jianshu_app', '0007_auto_20170726_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=2048, verbose_name='评论内容')),
                ('btime', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('star', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='评级')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_to_article', to='jianshu_app.Article', verbose_name='文章')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_to_owner', to=settings.AUTH_USER_MODEL, verbose_name='评论人')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]
