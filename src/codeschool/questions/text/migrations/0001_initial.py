# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-27 12:29
from __future__ import unicode_literals

import codeschool.lms.activities.models.activity
import codeschool.mixins
import codeschool.questions.models
import codeschool.vendor.wagtailmarkdown.blocks
from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.wagtailroutablepage.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activities', '0002_auto_20170627_0328'),
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextFeedback',
            fields=[
                ('feedback_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activities.Feedback')),
            ],
            options={
                'abstract': False,
            },
            bases=(codeschool.questions.models.QuestionMixin, 'activities.feedback'),
        ),
        migrations.CreateModel(
            name='TextProgress',
            fields=[
                ('progress_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activities.Progress')),
            ],
            options={
                'abstract': False,
            },
            bases=(codeschool.questions.models.QuestionMixin, 'activities.progress'),
        ),
        migrations.CreateModel(
            name='TextQuestion',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('short_description', models.CharField(help_text='A short textual description to be used in titles, lists, etc.', max_length=140, verbose_name='short description')),
                ('author_name', models.CharField(blank=True, help_text="The author's name, if not the same user as the question owner.", max_length=100, verbose_name="Author's name")),
                ('visible', models.BooleanField(default=codeschool.lms.activities.models.activity.bool_to_true, help_text='Makes activity invisible to users.', verbose_name='Invisible')),
                ('closed', models.BooleanField(default=bool, help_text='A closed activity does not accept new submissions, but users can see that they still exist.', verbose_name='Closed to submissions')),
                ('group_submission', models.BooleanField(default=bool, help_text='If enabled, submissions are registered to groups instead of individual students.', verbose_name='Group submissions')),
                ('max_group_size', models.IntegerField(default=6, help_text='If group submission is enabled, define the maximum size of a group.', verbose_name='Maximum group size')),
                ('disabled', models.BooleanField(default=bool, help_text='Activities can be automatically disabled when Codeshool encounters an error. This usually produces a message saved on the .disabled_message attribute. This field is not controlled directly by users.', verbose_name='Disabled')),
                ('disabled_message', models.TextField(blank=True, help_text='Messsage explaining why the activity was disabled.', verbose_name='Disabled message')),
                ('has_submissions', models.BooleanField(default=bool)),
                ('has_correct_submissions', models.BooleanField(default=bool)),
                ('body', wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('markdown', codeschool.vendor.wagtailmarkdown.blocks.MarkdownBlock()), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock())), blank=True, help_text='Describe what the question is asking and how should the students answer it as clearly as possible. Good questions should not be ambiguous.', null=True, verbose_name='Question description')),
                ('comments', wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='(Optional) Any private information that you want to associate to the question page.', verbose_name='Comments')),
                ('import_file', models.FileField(blank=True, help_text='Fill missing fields from question file. You can safely leave this blank and manually insert all question fields.', null=True, upload_to='question-imports', verbose_name='import question')),
                ('correct_answer', models.CharField(help_text='The expected Text answer for question.', max_length=100, verbose_name='Correct answer')),
                ('label', models.CharField(default='Answer', help_text='The label text that is displayed in the submission form.', max_length=100, verbose_name='Label')),
                ('help_text', models.TextField(blank=True, help_text='Additional explanation that is displayed under the input form.', verbose_name='Help text')),
            ],
            options={
                'verbose_name': 'Text question',
                'verbose_name_plural': 'Text questions',
            },
            bases=(codeschool.mixins.CommitMixin, wagtail.contrib.wagtailroutablepage.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='TextSubmission',
            fields=[
                ('submission_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activities.Submission')),
                ('value', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=(codeschool.questions.models.QuestionMixin, 'activities.submission'),
        ),
    ]
