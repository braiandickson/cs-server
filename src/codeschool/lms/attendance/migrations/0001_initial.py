# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-27 12:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.contrib.wagtailroutablepage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_attended', models.BooleanField(default=bool)),
                ('attempts', models.SmallIntegerField(default=int)),
            ],
        ),
        migrations.CreateModel(
            name='AttendancePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.wagtailroutablepage.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='AttendanceSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_attempts', models.SmallIntegerField(default=3, help_text='How many times a student can attempt to prove attendance. A maximum is necessary to avoid a brute force attack.', verbose_name='Maximum number of attempts')),
                ('expiration_minutes', models.SmallIntegerField(default=5, help_text='Time (in minutes) before attendance session expires.', verbose_name='Expiration time')),
                ('max_string_distance', models.SmallIntegerField(default=1, help_text='Maximum number of wrong characters that is considered acceptable when comparing the expected passphrase with the one given by thestudent.', verbose_name='Fuzzyness')),
                ('max_number_of_absence', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('created', models.DateTimeField()),
                ('expires', models.DateTimeField()),
                ('passphrase', models.CharField(help_text='The passphrase is case-insensitive. We tolerate small typing errors.', max_length=200, verbose_name='Passphrase')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceSheetChild',
            fields=[
                ('attendancesheet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='attendance.AttendanceSheet')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_sheet_single_list', to='attendance.AttendancePage')),
            ],
            bases=('attendance.attendancesheet',),
        ),
        migrations.AddField(
            model_name='event',
            name='sheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='attendance.AttendanceSheet'),
        ),
        migrations.AddField(
            model_name='attendancesheet',
            name='last_event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attendance.Event'),
        ),
        migrations.AddField(
            model_name='attendancesheet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attendancecheck',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Event'),
        ),
        migrations.AddField(
            model_name='attendancecheck',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
