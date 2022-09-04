# Generated by Django 3.2.15 on 2022-08-26 10:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(max_length=120)),
                ('note', models.TextField(blank=True, null=True)),
                ('boards', models.ManyToManyField(related_name='urlcards', related_query_name='urlcard', to='boards.Board')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urls', related_query_name='url', to='cards.urlcard')),
            ],
        ),
    ]