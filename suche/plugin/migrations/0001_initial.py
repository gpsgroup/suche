# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import plugin.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grammar',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('grammar', models.CharField(max_length=1024)),
                ('action', models.CharField(max_length=1024)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Plugin',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('plugin_type', models.CharField(max_length=128)),
                ('showsOp', models.BooleanField(default=False)),
                ('privateKey', models.CharField(max_length=512, default=plugin.models.randomGen)),
                ('pluginKey', models.CharField(max_length=512, default=plugin.models.randomGen)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('grammar', models.OneToOneField(to='plugin.Grammar')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
