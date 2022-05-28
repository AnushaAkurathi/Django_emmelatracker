# Generated by Django 3.1.14 on 2022-04-20 07:04

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=500, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Announcements',
                'db_table': 'announcements',
            },
        ),
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(max_length=200)),
                ('item', models.CharField(max_length=300)),
                ('bonus', models.FloatField(default='0')),
                ('member_id', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Bonus',
                'db_table': 'bonus',
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_no', models.IntegerField(default='0')),
                ('project_id', models.IntegerField(default='0')),
                ('task', models.CharField(max_length=400)),
                ('assigned_by', models.IntegerField(default='0')),
                ('assigned_to', models.IntegerField(default='0')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('instructions', models.TextField(default='None')),
                ('is_repeat', models.CharField(choices=[('0', '0'), ('1', '1')], default='0', max_length=20)),
                ('repeat_details', models.CharField(max_length=400)),
                ('subtask_id', models.IntegerField(default='null')),
                ('links', models.CharField(default='None', max_length=50)),
                ('is_valid', models.CharField(choices=[('0', '0'), ('1', '1')], default='1', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.IntegerField(null=True)),
                ('member', models.EmailField(blank=True, max_length=255)),
                ('member_firstname', models.EmailField(blank=True, max_length=255)),
                ('member_lastname', models.EmailField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Team',
                'db_table': 'team',
            },
        ),
        migrations.CreateModel(
            name='Worklogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField(default='0')),
                ('details_of_execution', models.TextField()),
                ('is_done', models.CharField(choices=[('0', '0'), ('1', '1')], default='0', max_length=20)),
                ('is_hold', models.CharField(choices=[('0', '0'), ('1', '1')], default='0', max_length=20)),
                ('member_id', models.IntegerField(default='0')),
                ('remarks', models.CharField(max_length=400)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('git_url', models.CharField(default='None', max_length=50)),
                ('gdocs_url', models.CharField(default='None', max_length=50)),
                ('other_links', models.CharField(default='None', max_length=50)),
                ('hours_taken', models.FloatField(default='0')),
                ('is_valid', models.CharField(choices=[('0', '0'), ('1', '1')], default='1', max_length=20)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Worklogs',
                'db_table': 'worklogs',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.CharField(choices=[('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'), ('105', '105'), ('106', '106'), ('None', 'None')], default='None', max_length=20)),
                ('reason', models.CharField(default='None', max_length=200)),
                ('details', models.CharField(default='None', max_length=200)),
                ('leave_for', models.FloatField(default='None')),
                ('typ_e', models.CharField(choices=[('Present', 'Present'), ('WFH', 'WFH'), ('Leave', 'Leave'), ('Break', 'Break'), ('None', 'None')], default='None', max_length=20)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('brea_k', models.CharField(choices=[('1 Hrs', '1 Hrs'), ('2 Hrs', '2 Hrs'), ('None', 'None')], default='None', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Attendence',
                'db_table': 'attendance',
                'unique_together': {('ids', 'date')},
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_director', models.BooleanField(default=False)),
                ('is_producer', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]