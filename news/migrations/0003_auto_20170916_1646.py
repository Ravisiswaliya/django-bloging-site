# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-16 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20170914_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctgry', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='nc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.Cat'),
        ),
    ]
