# Generated by Django 4.1.2 on 2022-11-28 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0018_alter_contactmodel_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='site',
            field=models.URLField(default=''),
        ),
    ]
