# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 07:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ta_app', '0002_task_detail'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task_detail',
            new_name='TaskDetail',
        ),
    ]
