# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-05-10 10:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tm500trf', '0057_auto_20180510_0804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testline',
            name='index',
        ),
    ]