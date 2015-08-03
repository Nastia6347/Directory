# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('picture', models.ImageField(upload_to=b'static/img')),
                ('slug', models.CharField(unique=True, max_length=70, editable=False)),
                ('parent', models.ForeignKey(blank=True, to='directory.Category', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('picture', models.ImageField(null=True, upload_to=b'static/img', blank=True)),
                ('slug', models.CharField(unique=True, max_length=70, editable=False)),
                ('category', models.ForeignKey(to='directory.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
