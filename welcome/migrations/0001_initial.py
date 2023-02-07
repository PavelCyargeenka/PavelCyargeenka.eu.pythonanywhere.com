# Generated by Django 4.1.2 on 2022-10-27 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('instrument', models.CharField(max_length=100)),
                ('slug', models.SlugField(default='')),
            ],
        ),
    ]
