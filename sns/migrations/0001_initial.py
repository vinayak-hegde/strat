# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-25 03:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Place', models.CharField(max_length=50)),
                ('Tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itype', models.CharField(max_length=10)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sns.Album')),
            ],
        ),
    ]
