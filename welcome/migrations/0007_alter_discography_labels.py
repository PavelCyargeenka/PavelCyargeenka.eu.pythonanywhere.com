# Generated by Django 4.1.2 on 2022-11-06 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0006_label_alter_discography_album_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discography',
            name='labels',
            field=models.ManyToManyField(related_name='albums', to='welcome.label'),
        ),
    ]
