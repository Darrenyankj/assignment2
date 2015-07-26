# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20150726_0246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='color',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='fontcolor',
        ),
    ]
