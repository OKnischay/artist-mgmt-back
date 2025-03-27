# Generated by Django 5.1.7 on 2025-03-27 09:31

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('album_name', models.CharField(max_length=255)),
                ('release_date', models.DateField(default=django.utils.timezone.now)),
                ('total_tracks', models.PositiveIntegerField(default=0)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='artists.artist')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
