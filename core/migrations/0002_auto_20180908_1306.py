# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-08 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountinvoice',
            name='s_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accountinvoice',
            name='s_tax',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accountinvoice',
            name='ss_tax',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accountinvoice',
            name='student_location',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accountinvoice',
            name='student_title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accountinvoice',
            name='tax',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accountinvoice',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
