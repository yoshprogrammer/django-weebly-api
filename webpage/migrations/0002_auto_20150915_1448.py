# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='principal',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='principal',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='principal',
            name='id',
            field=models.PositiveIntegerField(serialize=False, primary_key=True),
        ),
    ]
