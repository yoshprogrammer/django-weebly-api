# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.PositiveIntegerField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('test_mode', models.BooleanField(default=True)),
                ('language', models.TextField(default=b'en')),
            ],
        ),
        migrations.CreateModel(
            name='weebly_plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('term', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='weebly_site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_id', models.PositiveIntegerField(blank=True)),
                ('domain_name', models.URLField()),
                ('site_title', models.TextField(blank=True)),
                ('brand_name', models.TextField(blank=True)),
                ('brand_url', models.URLField(blank=True)),
                ('upgrade_url', models.URLField(blank=True)),
                ('publish_upsell_url', models.URLField(blank=True)),
                ('allow_ssl', models.BooleanField(default=True)),
            ],
        ),
    ]
