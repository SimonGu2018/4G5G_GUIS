# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-06-09 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tm500trf', '0060_auto_20180512_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='testline',
            name='cell',
            field=models.CharField(default='N/A', max_length=200),
        ),
    ]