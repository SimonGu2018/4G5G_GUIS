# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-02 07:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tm500trf', '0021_iperfcmd_iperfserver_tm500_ue_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='IperfCmd',
        ),
        migrations.DeleteModel(
            name='IperfServer',
        ),
        migrations.DeleteModel(
            name='TM500',
        ),
        migrations.DeleteModel(
            name='UE',
        ),
        migrations.DeleteModel(
            name='USER',
        ),
    ]
