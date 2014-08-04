# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linguistic', '0002_grammar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trigram',
            old_name='perplexity',
            new_name='probability',
        ),
        migrations.RenameField(
            model_name='bigram',
            old_name='perplexity',
            new_name='probability',
        ),
        migrations.AddField(
            model_name='word',
            name='probability',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
