# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch_change', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Poll',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='choice_test',
            new_name='choice',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='poll',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='question_text',
            new_name='question',
        ),
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(),
        ),
    ]
