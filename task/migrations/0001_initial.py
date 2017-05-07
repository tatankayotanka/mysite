# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 09:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.CharField(choices=[('NS', 'Not Started'), ('IP', 'In Progress'), ('FIN', 'Finished')], default='NS', max_length=2)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('deadline', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
