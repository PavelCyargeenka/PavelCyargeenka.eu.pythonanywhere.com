# Generated by Django 4.1.2 on 2022-10-29 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0002_discography'),
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_title', models.CharField(max_length=100)),
                ('song_number', models.IntegerField()),
                ('song_title', models.CharField(max_length=100)),
                ('slug', models.SlugField(default='')),
            ],
        ),
        migrations.AlterField(
            model_name='discography',
            name='album_year',
            field=models.IntegerField(),
        ),
    ]
