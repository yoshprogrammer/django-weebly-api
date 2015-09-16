# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0002_auto_20150915_1448'),
    ]

    operations = [
        migrations.DeleteModel(
            name='weebly_plan',
        ),
        migrations.DeleteModel(
            name='weebly_site',
        ),
    ]
