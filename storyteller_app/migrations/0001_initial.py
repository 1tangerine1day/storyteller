# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-10 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_post', models.CharField(max_length=25)),
                ('follow_who', models.CharField(max_length=25)),
                ('follow_created_id', models.CharField(max_length=25)),
                ('follow_created_at', models.CharField(max_length=25)),
                ('follow_likes', models.IntegerField(default=0)),
                ('follow_firstSentence', models.CharField(max_length=25)),
                ('follow_storyTitle', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('img', models.ImageField(default='default.jpg', upload_to='upload')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storyTitle', models.CharField(max_length=25)),
                ('created_id', models.CharField(max_length=25)),
                ('created_at', models.CharField(max_length=25)),
                ('created_day', models.CharField(max_length=25)),
                ('created_mon', models.CharField(max_length=25)),
                ('post_likes', models.IntegerField(default=0)),
                ('firstSentence', models.CharField(max_length=25)),
                ('created_auther', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=25)),
                ('auther', models.CharField(max_length=25)),
                ('post_id', models.IntegerField(default=0)),
                ('story_id', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('auther_img', models.ImageField(default='default.jpg', upload_to='upload')),
            ],
        ),
    ]
