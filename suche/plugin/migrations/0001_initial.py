# encoding: utf8
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('plugin_type', models.CharField(max_length=128)),
                ('showsOp', models.BooleanField(default=False)),
                ('grammar', models.OneToOneField(to_field='id', to='plugin.Grammar')),
                ('privateKey', models.CharField(default=plugin.models.randomGen, max_length=512)),
                ('pluginKey', models.CharField(default=plugin.models.randomGen, max_length=512)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
