# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=127)),
                ('last_name', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='Playgroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FootballMetric',
            fields=[
                ('player', models.OneToOneField(primary_key=True, serialize=False, to='matcher.Player')),
                ('defence', models.PositiveIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('midfield', models.PositiveIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('attack', models.PositiveIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='playgroup',
            field=models.ForeignKey(to='matcher.Playgroup'),
        ),
    ]
