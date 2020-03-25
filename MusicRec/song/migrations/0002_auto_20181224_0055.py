# Generated by Django 2.1 on 2018-12-23 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongLysic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_id', models.CharField(max_length=64, unique=True, verbose_name='歌曲ID')),
                ('song_lysic', models.TextField(blank=True, verbose_name='歌词')),
            ],
            options={
                'verbose_name_plural': '歌词信息',
                'db_table': 'songLysic',
            },
        ),
        migrations.RemoveField(
            model_name='song',
            name='song_lysic',
        ),
    ]
