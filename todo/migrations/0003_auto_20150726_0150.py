# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_todo_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('color', models.CharField(default=b'purple', max_length=50)),
                ('fontcolor', models.CharField(default=b'white', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('color', models.CharField(default=b'red', max_length=50)),
                ('fontcolor', models.CharField(default=b'black', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='todo',
            name='todo_date',
        ),
        migrations.AddField(
            model_name='todo',
            name='color',
            field=models.CharField(default=b'yellow', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todo',
            name='done',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todo',
            name='due',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todo',
            name='folder',
            field=models.ForeignKey(related_name='things', blank=True, to='todo.Folder', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todo',
            name='fontcolor',
            field=models.CharField(default=b'black', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todo',
            name='tag',
            field=models.ManyToManyField(related_name='things', null=True, to='todo.Tag', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todo',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='todo',
            name='content',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
