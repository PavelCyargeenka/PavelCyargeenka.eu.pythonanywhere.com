# Generated by Django 4.1.2 on 2022-10-28 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_title', models.CharField(max_length=100)),
                ('album_year', models.IntegerField(max_length=100)),
                ('slug', models.SlugField(default='')),
            ],
        ),
    ]
