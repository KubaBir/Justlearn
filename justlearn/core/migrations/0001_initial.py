# Generated by Django 4.0.10 on 2023-04-08 10:25

import core.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('link', models.URLField(default=None)),
                ('description', models.TextField(default='', max_length=510)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(default='', max_length=255)),
                ('description', models.TextField(default='', max_length=510)),
                ('duration', models.IntegerField(default=60)),
                ('lesson_date', models.DateTimeField(null=True)),
                ('meeting_link', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('proficiency', models.CharField(choices=[('JR', 'Junior'), ('MD', 'Mid'), ('SR', 'Senior')], default='JR', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github_link', models.URLField(blank=True, null=True)),
                ('linkedin_link', models.URLField(blank=True, null=True)),
                ('description', models.TextField(default='', max_length=510)),
                ('image', models.ImageField(null=True, upload_to=core.models.profile_pic_image_file_path)),
                ('rating', models.FloatField(default=0)),
                ('skills', models.ManyToManyField(to='core.skill')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github_link', models.URLField(blank=True, null=True)),
                ('linkedin_link', models.URLField(blank=True, null=True)),
                ('description', models.TextField(default='', max_length=510)),
                ('image', models.ImageField(null=True, upload_to=core.models.profile_pic_image_file_path)),
                ('skills', models.ManyToManyField(to='core.skill')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=255)),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('lessons', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=core.models.project_file_path)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('link', models.URLField(default=None)),
                ('description', models.TextField(max_length=510)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('advertisement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.advertisement')),
                ('problem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.problem')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.student')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.teacher'),
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=core.models.exercise_file_path)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.ManyToManyField(blank=True, to='core.message')),
                ('participants', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='advertisement',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.teacher'),
        ),
    ]
