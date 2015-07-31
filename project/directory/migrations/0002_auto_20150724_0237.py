# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=70, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=70, null=True),
            preserve_default=True,
        ),
    ]
