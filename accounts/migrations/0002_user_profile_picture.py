# Generated by Django 5.0.1 on 2024-01-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default=1, upload_to='profile_pics/'),
            preserve_default=False,
        ),
    ]