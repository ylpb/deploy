# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-03-18 04:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20200318_0334'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeployTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=32, verbose_name='标识')),
                ('tag', models.CharField(max_length=32, verbose_name='版本')),
                ('status', models.IntegerField(choices=[(1, '待发布'), (2, '发布中'), (3, '成功'), (4, '失败')], default=1, verbose_name='状态')),
                ('before_download_script', models.TextField(blank=True, null=True, verbose_name='下载前脚本')),
                ('after_download_script', models.TextField(blank=True, null=True, verbose_name='下载后脚本')),
                ('before_deploy_script', models.TextField(blank=True, null=True, verbose_name='发布前脚本')),
                ('after_deploy_script', models.TextField(blank=True, null=True, verbose_name='发布后脚本')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Project', verbose_name='项目')),
            ],
        ),
    ]