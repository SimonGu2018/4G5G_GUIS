# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-15 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tm500trf', '0044_delete_tm500'),
    ]

    operations = [
        migrations.CreateModel(
            name='TM500',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('tma', models.GenericIPAddressField()),
                ('index', models.CharField(max_length=4)),
                ('pppoenum', models.CharField(max_length=3)),
                ('pppidx', models.CharField(max_length=50)),
                ('startip', models.GenericIPAddressField()),
                ('endip', models.GenericIPAddressField()),
                ('pppaction', models.CharField(max_length=5)),
                ('pppstatus', models.CharField(max_length=20)),
            ],
        ),
    ]
