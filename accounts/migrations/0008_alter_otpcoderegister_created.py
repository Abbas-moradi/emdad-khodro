# Generated by Django 5.0.1 on 2024-01-23 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_otpcoderegister_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpcoderegister',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
