# Generated by Django 4.1.2 on 2022-11-30 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0020_delete_contactmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp_bio', models.TextField(default='')),
            ],
        ),
    ]
