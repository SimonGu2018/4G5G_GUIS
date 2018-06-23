# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-01 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tm500trf', '0015_delete_tputinfo'),
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
                ('user', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20)),
                ('ppp', models.CharField(max_length=20)),
                ('ul_cmd', models.CharField(max_length=100)),
                ('dl_cmd', models.CharField(max_length=100)),
                ('ul_status', models.CharField(max_length=10)),
                ('dl_status', models.CharField(max_length=10)),
                ('tm500', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='TM500Info',
        ),
        migrations.DeleteModel(
            name='UEInfo',
        ),
    ]