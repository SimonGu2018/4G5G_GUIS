# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-03 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tm500trf', '0034_auto_20170303_0812'),
    ]

    operations = [
        migrations.CreateModel(
            name='NIC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adapter', models.CharField(max_length=10)),
                ('nic', models.CharField(max_length=10)),
            ],
        ),
    ]
