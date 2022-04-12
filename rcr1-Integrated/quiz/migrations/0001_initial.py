# Generated by Django 4.0.2 on 2022-04-12 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('questiondesc', models.TextField(blank=True, null=True)),
                ('answer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='riddle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riddle', models.CharField(max_length=500)),
                ('riddledesc', models.TextField(blank=True, null=True)),
                ('answer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='userlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unattemptedlist', models.TextField()),
                ('attemptedlist', models.TextField(blank=True, null=True)),
                ('correctlist', models.TextField(blank=True, null=True)),
                ('attemptsleft', models.IntegerField(default=2)),
                ('markingscheme', models.CharField(default='4,2', max_length=100)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response1', models.CharField(max_length=200)),
                ('response2', models.CharField(max_length=200)),
                ('r1_time', models.DateTimeField(null=True)),
                ('r2_time', models.DateTimeField(null=True)),
                ('queid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
