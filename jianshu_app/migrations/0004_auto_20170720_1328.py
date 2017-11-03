# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jianshu_app', '0003_uarticle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uarticle',
            old_name='Content',
            new_name='content',
        ),
    ]
