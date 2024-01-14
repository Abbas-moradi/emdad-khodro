# Generated by Django 5.0.1 on 2024-01-14 13:54

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('phone', models.CharField(max_length=12, unique=True)),
                ('full_name', models.CharField(max_length=150)),
                ('job_type', models.CharField(choices=[('MR', 'Mechanical Repair'), ('ER', 'Electrical Repair'), ('BW', 'Body Work'), ('PT', 'Painting'), ('TR', 'Transmission Repair'), ('OC', 'Oil Change'), ('TW', 'Towing'), ('OT', 'Other')], default='OT', max_length=2)),
                ('city', models.CharField(choices=[('AB', 'Abyek')], default='AB', max_length=2)),
                ('is_active', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=250)),
                ('subject', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='OtpCodeRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12)),
                ('code', models.PositiveSmallIntegerField()),
                ('created', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('subject', models.CharField(max_length=250)),
                ('status', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
    ]