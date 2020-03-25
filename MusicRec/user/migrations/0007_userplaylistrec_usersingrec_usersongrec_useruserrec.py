# Generated by Django 2.1 on 2019-01-05 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_usersim'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPlayListRec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=64, verbose_name='用户ID')),
                ('related', models.CharField(blank=True, max_length=64, verbose_name='歌单ID')),
                ('sim', models.FloatField(blank=True, verbose_name='相似度')),
            ],
            options={
                'verbose_name_plural': '用户歌单推荐',
                'db_table': 'UserPlayListRec',
            },
        ),
        migrations.CreateModel(
            name='UserSingRec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=64, verbose_name='用户ID')),
                ('related', models.CharField(blank=True, max_length=64, verbose_name='歌手ID')),
                ('sim', models.FloatField(blank=True, verbose_name='相似度')),
            ],
            options={
                'verbose_name_plural': '用户歌手推荐',
                'db_table': 'UserSingRec',
            },
        ),
        migrations.CreateModel(
            name='UserSongRec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=64, verbose_name='用户ID')),
                ('related', models.CharField(blank=True, max_length=64, verbose_name='歌曲ID')),
                ('sim', models.FloatField(blank=True, verbose_name='相似度')),
            ],
            options={
                'verbose_name_plural': '用户歌曲推荐',
                'db_table': 'UserSongRec',
            },
        ),
        migrations.CreateModel(
            name='UserUserRec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=64, verbose_name='用户ID')),
                ('related', models.CharField(blank=True, max_length=64, verbose_name='用户ID')),
                ('sim', models.FloatField(blank=True, verbose_name='相似度')),
            ],
            options={
                'verbose_name_plural': '用户用户推荐',
                'db_table': 'UserUserRec',
            },
        ),
    ]
