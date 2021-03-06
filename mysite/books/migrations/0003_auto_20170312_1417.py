# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20170311_0237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='headshot',
        ),
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='salutation',
        ),
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(default=None, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='e-mail'),
        ),
    ]
