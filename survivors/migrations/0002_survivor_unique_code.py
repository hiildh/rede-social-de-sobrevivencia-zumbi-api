# Generated by Django 5.0.3 on 2024-06-06 22:38

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survivors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survivor',
            name='unique_code',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
