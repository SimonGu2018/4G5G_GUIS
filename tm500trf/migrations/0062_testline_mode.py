# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-06-09 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tm500trf', '0061_testline_cell'),
    ]

    operations = [
        migrations.AddField(
            model_name='testline',
            name='mode',
            field=models.CharField(default='N/A', max_length=200),
        ),
    ]