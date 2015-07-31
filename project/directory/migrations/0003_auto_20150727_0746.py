# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_auto_20150724_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(related_name=b'child', blank=True, to='directory.Category', null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='picture',
            field=models.ImageField(upload_to=b'static/img'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=70, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'static/img', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=70, null=True, blank=True),
        ),
    ]
