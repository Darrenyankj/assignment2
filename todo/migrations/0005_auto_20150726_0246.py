# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20150726_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='color',
            field=models.CharField(default=b'yellow', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todo',
            name='fontcolor',
            field=models.CharField(default=b'black', max_length=50),
            preserve_default=True,
        ),
    ]
