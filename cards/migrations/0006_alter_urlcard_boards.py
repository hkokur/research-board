# Generated by Django 3.2.15 on 2022-08-30 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_rename_decription_board_description'),
        ('cards', '0005_alter_urlcard_boards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlcard',
            name='boards',
            field=models.ManyToManyField(related_name='urlcards', related_query_name='urlcard', to='boards.Board'),
        ),
    ]