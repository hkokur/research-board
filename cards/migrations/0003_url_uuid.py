# Generated by Django 3.2.15 on 2022-08-30 08:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_alter_urlcard_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
