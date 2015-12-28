# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('md5', models.CharField(unique=True, max_length=32)),
                ('name', models.CharField(max_length=64)),
                ('extension', models.CharField(max_length=16)),
                ('path', models.CharField(max_length=128)),
            ],
        ),
    ]
