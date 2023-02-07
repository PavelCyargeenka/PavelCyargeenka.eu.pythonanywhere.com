# Generated by Django 4.1.2 on 2022-11-21 22:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0014_remove_albums_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3)])),
                ('e_mail', models.EmailField(default='', max_length=254)),
                ('message', models.TextField(max_length=150)),
            ],
        ),
    ]
