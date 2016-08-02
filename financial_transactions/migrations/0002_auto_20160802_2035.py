# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.fields as fields
from django.db.migrations.migration import Migration
from django.db.migrations.operations.fields import AddField


class PayeeMigration(Migration):
    initial = True

    dependencies = [
        ('financial_transactions', '0001_initial'),
    ]

    operations = [
        AddField(
            model_name='Transaction',
            name='payee',
            field=fields.TextField(verbose_name='Payee'),
        ),
    ]
