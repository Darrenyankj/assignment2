# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20150726_0150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='color',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='fontcolor',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='color',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='fontcolor',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='color',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='fontcolor',
        ),
    ]
