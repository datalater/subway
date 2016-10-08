# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 14:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0005_auto_20161001_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Recent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatbot.Line')),
            ],
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='subway',
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Subway',
        ),
        migrations.AddField(
            model_name='recent',
            name='station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chatbot.Station'),
        ),
        migrations.AddField(
            model_name='recent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatbot.User'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chatbot.Station'),
        ),
    ]
