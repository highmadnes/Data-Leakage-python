# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataApp', '0007_request_checked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='rabin',
            field=models.CharField(max_length=100),
        ),
    ]
