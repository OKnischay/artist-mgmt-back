# Generated by Django 5.1.7 on 2025-03-18 07:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='release_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
