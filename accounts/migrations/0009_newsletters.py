# Generated by Django 5.0.1 on 2024-01-24 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_otpcoderegister_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'newslletter',
                'verbose_name_plural': 'newslletters',
                'ordering': ['created'],
            },
        ),
    ]
