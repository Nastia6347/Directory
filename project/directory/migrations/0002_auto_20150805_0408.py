# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=70, unique=True, null=True, editable=False, blank=True),
        ),
    ]
