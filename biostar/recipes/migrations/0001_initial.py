# Generated by Django 2.2 on 2019-07-20 03:11

import biostar.recipes.models
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
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('security', models.IntegerField(choices=[(1, 'All users may run recipe'), (2, 'Only moderators may run recipe')], default=2)),
                ('deleted', models.BooleanField(default=False)),
                ('uid', models.CharField(max_length=32, unique=True)),
                ('name', models.CharField(default='My Recipe', max_length=256)),
                ('text', models.TextField(default='This is the recipe description.', max_length=10000)),
                ('html', models.TextField(default='html')),
                ('rank', models.FloatField(default=100)),
                ('lastedit_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('diff_date', models.DateField(auto_now_add=True)),
                ('json_text', models.TextField(default='{}', max_length=10000)),
                ('template', models.TextField(default='')),
                ('last_valid', models.TextField(default='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, default=None, help_text='Optional image', max_length=1024, upload_to=biostar.recipes.models.image_path)),
                ('diff_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='diff_author', to=settings.AUTH_USER_MODEL)),
                ('lastedit_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='analysis_editor', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.FloatField(default=100)),
                ('lastedit_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('privacy', models.IntegerField(choices=[(3, 'Private'), (2, 'Shareable Link'), (1, 'Public')], default=3)),
                ('image', models.ImageField(blank=True, default=None, max_length=1024, upload_to=biostar.recipes.models.image_path)),
                ('name', models.CharField(default='New Project', max_length=256)),
                ('deleted', models.BooleanField(default=False)),
                ('text', models.TextField(default='Project description.', max_length=10000)),
                ('html', models.TextField(default='html', max_length=200000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('uid', models.CharField(max_length=32, unique=True)),
                ('lastedit_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proj_editor', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(1, 'Queued'), (2, 'Running'), (6, 'Paused'), (5, 'Spooled'), (3, 'Completed'), (4, 'Error')], default=1)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(default='New results', max_length=256)),
                ('image', models.ImageField(blank=True, default=None, max_length=1024, upload_to=biostar.recipes.models.image_path)),
                ('lastedit_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.TextField(default='Result description.', max_length=10000)),
                ('html', models.TextField(default='html')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('json_text', models.TextField(default='commands')),
                ('uid', models.CharField(max_length=32)),
                ('template', models.TextField(default='makefile')),
                ('security', models.IntegerField(choices=[(1, 'Authorized'), (2, 'Authorization Required')], default=2)),
                ('script', models.TextField(default='')),
                ('stdout_log', models.TextField(default='', max_length=200000)),
                ('stderr_log', models.TextField(default='', max_length=200000)),
                ('valid', models.BooleanField(default=True)),
                ('path', models.FilePathField(default='')),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Analysis')),
                ('lastedit_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_editor', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(1, 'Pending'), (2, 'Ready'), (3, 'Error')], default=1)),
                ('method', models.IntegerField(choices=[(1, 'Linked Data'), (2, 'Uploaded Data'), (3, 'Text Field')], default=1)),
                ('name', models.CharField(default='My Data', max_length=256)),
                ('image', models.ImageField(blank=True, default=None, max_length=1024, upload_to=biostar.recipes.models.image_path)),
                ('deleted', models.BooleanField(default=False)),
                ('rank', models.FloatField(default=100)),
                ('lastedit_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.TextField(blank=True, default='Data description.', max_length=10000)),
                ('html', models.TextField(default='html')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(default='DATA', max_length=256)),
                ('size', models.BigIntegerField(default=0)),
                ('file', models.FilePathField(max_length=1024)),
                ('uid', models.CharField(max_length=32, unique=True)),
                ('lastedit_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_editor', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Project')),
            ],
        ),
        migrations.AddField(
            model_name='analysis',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Project'),
        ),
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access', models.IntegerField(choices=[(1, 'No Access'), (2, 'Read Access'), (3, 'Write Access')], db_index=True, default=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
