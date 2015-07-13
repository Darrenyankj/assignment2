# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='todo_date',
            field=models.DateField(default=datetime.datetime(2015, 7, 7, 8, 14, 34, 685617, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
