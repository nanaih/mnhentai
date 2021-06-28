# Generated by Django 3.2.4 on 2021-06-28 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmnhentai', '0002_doujinshi_is_translated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artists',
            old_name='artist_id',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='artists',
            old_name='doujinshi_id',
            new_name='doujinshi',
        ),
        migrations.RenameField(
            model_name='characters',
            old_name='character_id',
            new_name='character',
        ),
        migrations.RenameField(
            model_name='characters',
            old_name='doujinshi_id',
            new_name='doujinshi',
        ),
        migrations.RenameField(
            model_name='doujinshi',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='doujinshi',
            old_name='language_id',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='groups',
            old_name='doujinshi_id',
            new_name='doujinshi',
        ),
        migrations.RenameField(
            model_name='groups',
            old_name='group_id',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='parodys',
            old_name='doujinshi_id',
            new_name='doujinshi',
        ),
        migrations.RenameField(
            model_name='parodys',
            old_name='parody_id',
            new_name='parody',
        ),
        migrations.RenameField(
            model_name='tags',
            old_name='doujinshi_id',
            new_name='doujinshi',
        ),
        migrations.RenameField(
            model_name='tags',
            old_name='tag_id',
            new_name='tag',
        ),
        migrations.RemoveField(
            model_name='doujinshi',
            name='URL',
        ),
        migrations.AddField(
            model_name='doujinshi',
            name='dir_path',
            field=models.CharField(default='', max_length=512),
            preserve_default=False,
        ),
    ]
